import os
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

# =====================================
# /start
# =====================================
@bot.message_handler(commands=['start'])
def boas_vindas(mensagem):
    bot.reply_to(mensagem, "Olá, como posso te ajudar?\nClique em uma das opções abaixo:\n\n/investimento\n/banco")

# =====================================
# /investimento
# =====================================
@bot.message_handler(commands=['investimento'])
def investimento(mensagem):
    bot.reply_to(mensagem, "Clique em uma das opções abaixo:\n/duvidas\n/render")

# =====================================
# /duvidas
# =====================================
@bot.message_handler(commands=['duvidas'])
def duvidas(mensagem):
    bot.reply_to(mensagem, "Clique em uma das opções abaixo:\n/cdi\n/juroscompostos\n/selic\n/inflacao\n/rendafixa")

# =====================================
# Respostas de investimento
# =====================================
@bot.message_handler(commands=['cdi'])
def cdi(mensagem):
    bot.reply_to(mensagem, "CDI é uma taxa de referência usada como base para vários investimentos.")

@bot.message_handler(commands=['juroscompostos'])
def juros_compostos(mensagem):
    bot.reply_to(mensagem, "Juros compostos fazem o dinheiro crescer de forma exponencial.")

@bot.message_handler(commands=['selic'])
def selic(mensagem):
    bot.reply_to(mensagem, "A Selic é a taxa que guia os juros no Brasil.")

@bot.message_handler(commands=['inflacao'])
def inflacao(mensagem):
    bot.reply_to(mensagem, "Infação corrói o valor do dinheiro.")

@bot.message_handler(commands=['rendafixa'])
def renda_fixa(mensagem):
    bot.reply_to(mensagem, "Renda fixa tem previsibilidade maior de retorno.")

# =====================================
# /banco
# =====================================
@bot.message_handler(commands=['banco'])
def banco(mensagem):
    bot.reply_to(mensagem, "Digite em uma das opções abaixo:\n/saldo\n/depositar (valor)\n/sacar (valor)")


# =====================================
# /saldo
# =====================================
saldo = 0

@bot.message_handler(commands=['saldo'])
def ver_saldo(mensagem):
    bot.reply_to(mensagem, f"Seu saldo atual é de R${saldo:.2f}")

# =====================================
# /depositar
# =====================================
@bot.message_handler(commands=['depositar'])
def depositar(mensagem):
    global saldo
    
    try:
        valor = float(mensagem.text.split()[1])
        saldo += valor
        bot.reply_to(mensagem, f"Depósito realizado! Novo saldo: R${saldo:.2f}")
    
    except:
        bot.reply_to(mensagem, "Use: /depositar (valor)")

# =====================================
# /sacar
# =====================================
@bot.message_handler(commands=['sacar'])
def sacar(mensagem):
    global saldo
    
    try:
        valor = float(mensagem.text.split()[1])
        
        if valor > saldo:
            bot.reply_to(mensagem, "Saldo insuficiente! Tente novamente")
        else:
            saldo -= valor
            bot.reply_to(mensagem, f"Saque realizado! Novo saldo: R${saldo:.2f}")
    
    except:
        bot.reply_to(mensagem, "Use: /sacar (valor)")


# =====================================
# /render
# =====================================
@bot.message_handler(commands=['render'])
def simulador_juros_composto(mensagem):

    try:
        partes = mensagem.text.split()

        valor = float(partes[1])
        meses = int(partes[2])
        taxa = float(partes[3])

        if valor <= 0 or meses <= 0:
            bot.reply_to(mensagem, "O valor inserido e a quantidade de meses devem ser maiores que zero")
            return
        
        montante = valor * (1 + taxa) ** meses
        lucro = montante - valor

        bot.reply_to(
            mensagem,
            f"📊 Simulação de Investimento com Juros Composto\n\n"
            f"Valor investido: R${valor:.2f}\n"
            f"Meses: {meses}\n"
            f"Taxa: {taxa}% ao mês\n"
            f"Valor final: R${montante:.2f}\n"
            f"Lucro: R${lucro:.2f}"
            )
        
    except:
        bot.reply_to(mensagem, "Use: /render (valor) (meses) (taxa)")


# =============================================================
# Responde, caso não seja nenhum comando digitado seja válido
# =============================================================
@bot.message_handler(func=lambda msg: True)
def echo_all(mensagem):
    bot.reply_to(mensagem, "Comando inválido. Digite /start para começar.")


print("BOT iniciado com sucesso!")

bot.infinity_polling()