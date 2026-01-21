# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from game_data import historia # Importando história

app = Flask(__name__)
app.config['SECRET_KEY'] = 'semlivro'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livrojogo.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- MODELOS DO BANCO DE DADOS ---
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    save_game = db.relationship('SaveGame', backref='user', uselist=False)

class SaveGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    current_scene = db.Column(db.String(50), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- ROTAS ---

# Rota Inicial / Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        # Simples verificação (em produção use hash de senha!)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login inválido.')
            
    return render_template('index.html')

# 2. Dashboard (Lista de Livros)
@app.route('/dashboard')
@login_required
def dashboard():
    tem_save = False
    if current_user.save_game:
        tem_save = True
    return render_template('dashboard.html', tem_save=tem_save)

# 3. Lógica de Iniciar/Continuar
@app.route('/setup_game/<acao>')
@login_required
def setup_game(acao):
    if acao == 'novo':
        # NOVA LÓGICA:
        # Se o usuário já tem um save, RESETA ele para o início.
        if current_user.save_game:
            current_user.save_game.current_scene = 'inicio'
            db.session.commit() # Salva a atualização
        else:
            # Se não tem save nenhum, cria um novo
            novo_save = SaveGame(user_id=current_user.id, current_scene='inicio')
            db.session.add(novo_save)
            db.session.commit()
            
        return redirect(url_for('jogar', cena_id='inicio'))
        
    elif acao == 'continuar':
        if current_user.save_game:
            cena = current_user.save_game.current_scene
            return redirect(url_for('jogar', cena_id=cena))
        else:
            return redirect(url_for('dashboard'))

# 4. A Tela do Jogo (Engine)
@app.route('/jogar/<cena_id>')
@login_required
def jogar(cena_id):
    # Verifica se a cena existe
    dados_cena = historia.get(cena_id)
    
    if not dados_cena:
        return "Erro: Cena não encontrada."

    # Salva o progresso automaticamente a cada passo
    if current_user.save_game:
        current_user.save_game.current_scene = cena_id
        db.session.commit()
    else:
        # Fallback caso algo dê errado
        novo_save = SaveGame(user_id=current_user.id, current_scene=cena_id)
        db.session.add(novo_save)
        db.session.commit()

    return render_template('game.html', cena=dados_cena, cena_atual=cena_id)

# 5. Rota para criar banco (apenas para teste inicial)
@app.route('/criar_banco')
def criar_banco():
    with app.app_context():
        db.create_all()
        # Cria um usuário de teste
        if not User.query.filter_by(username='admin').first():
            user = User(username='admin', password='Acb#231')
            db.session.add(user)
            db.session.commit()
    return "Banco criado e usuário 'admin' (senha Acb#231) adicionado."

if __name__ == '__main__':
    app.run(debug=True)