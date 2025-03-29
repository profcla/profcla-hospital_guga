import streamlit as st
import random
from base64 import b64encode

# Configuração inicial
st.set_page_config(page_title="Hospital Guga", page_icon="🏥")

# Sons
CORRETO_SOUND = "https://cdn.pixabay.com/download/audio/2021/08/09/audio_7a38d8d9a4.mp3?filename=success-1-6297.mp3"
ERRO_SOUND = "https://cdn.pixabay.com/download/audio/2021/08/04/audio_3d35561c4e.mp3?filename=wrong-47985.mp3"
VITORIA_SOUND = "https://cdn.pixabay.com/download/audio/2023/04/12/audio_3b5d1c5c5e.mp3?filename=success-fanfare-trumpets-6185.mp3"

# Recursos
MEDICO_IMG = "👨⚕️"
DIRETOR_IMG = "🎩"
PONTUACAO_MAXIMA = 30

# Banco de dados
doencas = [
    {"nome": "Gripe", "sintomas": "Febre, tosse, dor no corpo", "icone": ""},
    {"nome": "Dengue", "sintomas": "Febre alta, dor ocular, manchas", "icone": ""},
    {"nome": "Conjuntivite", "sintomas": "Olhos vermelhos, coceira", "icone": ""},
    {"nome": "Hipertensão", "sintomas": "Pressão alta, tontura", "icone": ""},
    {"nome": "Diabetes", "sintomas": "Sede excessiva, visão turva", "icone": ""},
    {"nome": "COVID-19", "sintomas": "Febre, tosse seca, perda de paladar", "icone": ""},
    {"nome": "Resfriado", "sintomas": "Coriza, espirros, congestão nasal", "icone": ""},
    {"nome": "Asma", "sintomas": "Falta de ar, chiado no peito", "icone": ""},
    {"nome": "Bronquite", "sintomas": "Tosse com catarro, fadiga", "icone": ""},
    {"nome": "Pneumonia", "sintomas": "Febre alta, dificuldade respiratória", "icone": ""},
    {"nome": "Rinite", "sintomas": "Espirros frequentes, coceira no nariz", "icone": ""},
    {"nome": "Sinusite", "sintomas": "Dor facial, congestão, dor de cabeça", "icone": ""},
    {"nome": "Anemia", "sintomas": "Fadiga, palidez, fraqueza", "icone": ""},
    {"nome": "Enxaqueca", "sintomas": "Dor de cabeça intensa, sensibilidade à luz", "icone": ""},
    {"nome": "Hepatite", "sintomas": "Pele amarelada, fadiga, náuseas", "icone": ""},
    {"nome": "Tuberculose", "sintomas": "Tosse persistente, suor noturno, perda de peso", "icone": ""},
    {"nome": "Artrite", "sintomas": "Dor nas articulações, inchaço", "icone": ""},
    {"nome": "Gastrite", "sintomas": "Dor abdominal, indigestão, azia", "icone": ""},
    {"nome": "Insônia", "sintomas": "Dificuldade para dormir, fadiga diurna", "icone": ""},
    {"nome": "Varicela", "sintomas": "Erupções cutâneas, coceira, febre", "icone": ""},
    {"nome": "Caxumba", "sintomas": "Inchaço nas glândulas salivares, febre", "icone": ""},
    {"nome": "Sarampo", "sintomas": "Manchas vermelhas, febre alta, tosse", "icone": ""},
    {"nome": "Meningite", "sintomas": "Rigidez no pescoço, fotofobia, dor de cabeça", "icone": ""},
    {"nome": "Leptospirose", "sintomas": "Febre, dor muscular, icterícia", "icone": ""},
    {"nome": "Lúpus", "sintomas": "Erupção facial, fadiga, dor nas articulações", "icone": ""},
    {"nome": "Labirintite", "sintomas": "Tontura, vertigem, náuseas", "icone": ""},
    {"nome": "Mononucleose", "sintomas": "Fadiga extrema, dor de garganta, ínguas", "icone": ""},
    {"nome": "Doença de Crohn", "sintomas": "Dor abdominal, diarreia crônica", "icone": ""},
    {"nome": "Fibromialgia", "sintomas": "Dor muscular generalizada, pontos doloridos", "icone": ""},
    {"nome": "Psoríase", "sintomas": "Placas vermelhas na pele, descamação", "icone": ""},
    {"nome": "Malária", "sintomas": "Febre intermitente, calafrios", "icone": "", "gravidade": "Grave"}
]

personagens = {
    "médico": {"nome": "Dr. Gustavo", "imagem": MEDICO_IMG},
    "pacientes": [
        {"nome": "Clara", "imagem": "👩🦰", "idade": random.randint(20, 40)},
        {"nome": "Pedro", "imagem": "👨🦱", "idade": random.randint(30, 50)},
        {"nome": "Ana", "imagem": "👩🦳", "idade": random.randint(60, 80)},
        {"nome": "Guga", "imagem": "👨🦲", "idade": random.randint(25, 45)},
        {"nome": "Mariana", "imagem": "👩⚕️", "idade": random.randint(25, 35)},
        {"nome": "Rafael", "imagem": "👨🍳", "idade": random.randint(35, 55)},
        {"nome": "Lúcia", "imagem": "👵", "idade": random.randint(70, 85)},
        {"nome": "Tiago", "imagem": "👨🎓", "idade": random.randint(18, 25)},
        {"nome": "Beatriz", "imagem": "👩🎤", "idade": random.randint(20, 30)},
        {"nome": "Carlos", "imagem": "👨🚀", "idade": random.randint(40, 60)},
        {"nome": "Fernanda", "imagem": "👩🚒", "idade": random.randint(25, 40)},
        {"nome": "Roberto", "imagem": "👨✈️", "idade": random.randint(45, 65)},
        {"nome": "Isabela", "imagem": "👩🎨", "idade": random.randint(18, 28)},
        {"nome": "Antônio", "imagem": "👨🌾", "idade": random.randint(50, 70)}
    ]
}

def play_sound(url):
    """Reproduz som a partir de uma URL"""
    audio_html = f'<audio autoplay><source src="{url}" type="audio/mpeg"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

# Inicialização do estado
if 'game_data' not in st.session_state:
    st.session_state.game_data = {
        'pontuacao': 0,
        'salario': 5000,
        'paciente_atual': None,
        'opcoes': [],
        'feedback': None
    }

def novo_paciente():
    """Gera novo paciente com elementos aleatórios"""
    paciente = random.choice(personagens["pacientes"])
    doenca = random.choice(doencas)
    
    opcoes = random.sample(doencas, 3)
    while doenca not in opcoes:
        opcoes = random.sample(doencas, 3)
    random.shuffle(opcoes)
    
    st.session_state.game_data.update({
        'paciente_atual': {
            "dados": paciente,
            "doenca": doenca
        },
        'opcoes': opcoes,
        'feedback': None
    })

def verificar_resposta(resposta):
    """Processa resposta com efeitos sonoros"""
    data = st.session_state.game_data
    doenca_correta = data['paciente_atual']['doenca']
    
    if resposta == doenca_correta["nome"]:
        data['pontuacao'] += 1
        bonus = random.uniform(0.08, 0.15)
        data['salario'] *= (1 + bonus)
        data['feedback'] = ('success', f"✅ Correto! +R${data['salario'] * bonus:,.2f} de bônus")
        play_sound(CORRETO_SOUND)
    else:
        penalidade = random.uniform(0.05, 0.10)
        data['salario'] *= (1 - penalidade)
        data['feedback'] = ('error', f"❌ Errado! Diagnóstico correto: {doenca_correta['nome']} | -R${data['salario'] * penalidade:,.2f}")
        play_sound(ERRO_SOUND)
    
    st.session_state.game_data = data

# Interface
st.title("🏥 Hospital do Guga ")

# Jogo principal
if st.session_state.game_data['pontuacao'] < PONTUACAO_MAXIMA:
    data = st.session_state.game_data
    if not data['paciente_atual']:
        novo_paciente()
        st.rerun()

    paciente = data['paciente_atual']['dados']
    doenca = data['paciente_atual']['doenca']
    
    # Layout do paciente
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Médico")
        st.markdown(f"### {personagens['médico']['imagem']} {personagens['médico']['nome']}")
        
    with col2:
        st.subheader("Paciente")
        st.markdown(f"### {paciente['imagem']} {paciente['nome']} ({paciente['idade']} anos)")
    
    # Sintomas
    st.divider()
    st.subheader(f"{doenca['icone']} Sintomas:")
    st.write(f"**{doenca['sintomas']}**")
    
    # Opções
    st.divider()
    st.subheader("Diagnóstico:")
    
    for opcao in data['opcoes']:
        if st.button(
            f"{opcao['icone']} {opcao['nome']}",
            key=opcao['nome'],
            on_click=verificar_resposta,
            args=(opcao['nome'],)
        ):
            pass

    # Seção final do dashboard
    st.divider()
    
    # Feedback e status
    if data['feedback']:
        tipo, mensagem = data['feedback']
        if tipo == 'success':
            st.success(mensagem)
        else:
            st.error(mensagem)
        
        # Status atualizado
        st.markdown(f"""
        📊 **Progresso:** {data['pontuacao']}/{PONTUACAO_MAXIMA} pacientes
        💰 **Salário Atual:** R${data['salario']:,.2f}
        """)
        
        if st.button("Próximo Paciente →", key="proximo"):
            novo_paciente()
            st.rerun()

else:
    st.balloons()
    play_sound(VITORIA_SOUND)
    st.success(f"## {DIRETOR_IMG} Parabéns! Você é o novo Diretor do Hospital Guga!")
    st.markdown(f"### Salário final: R${st.session_state.game_data['salario']:,.2f}")
    
    # Animação de confetes
    st.markdown("""
    <style>
    @keyframes confetti {
        0% { transform: translateY(-100vh) rotate(0deg); }
        100% { transform: translateY(100vh) rotate(360deg); }
    }
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background: #ff0000;
        animation: confetti 2s linear infinite;
    }
    </style>
    <div class="confetti" style="left:10%"></div>
    <div class="confetti" style="left:30%"></div>
    <div class="confetti" style="left:50%"></div>
    <div class="confetti" style="left:70%"></div>
    <div class="confetti" style="left:90%"></div>
    """, unsafe_allow_html=True)
    
    if st.button("Jogar novamente"):
        st.session_state.clear()
        st.rerun()