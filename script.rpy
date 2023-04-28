# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define main = Character("Irgos Braço-Forte")
define stranger = Character("Estranho")

define ravisin = Character("Ravisin")
define rahrz = Character("Rahrz")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene icewind-dale

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # History Context

    "Você está no Vale do Vento Gélido, uma tundra repleta de planíces de neve e gelo, murada por montanhas imensas, que formam a Espinha do Mundo."
    "Embora possua um clima inóspito, diversos assentamentos foram montados ao longo dos anos. Esse conjunto de assentamentos no meio de toda a tundra é conhecido por Dez-Cidades."

    # Character Presentation

    show goliath

    "Você é Irgos Braço-Forte, um poderoso guerreiro golias. Equipado apenas com seu machado cru e um pacote de suprimentos básicos, você se esforça para sobreviver nessa terra congelada."
    "Os motivos que te trouxeram até esta terra desolante são desconhecidos, assim como as ações de sua vida passada. Prepare-se, pois sua aventura, nas vastas terras congeladas, começa agora."
    # Scene 1

    scene tundra

    "Você está descansando, em um acampamento temporário que você fez na encrosta de uma colina. Você revira seus alforges, e vê-se obrigado a passar o dia com um pacote de carne-seca, o último que você possui."

    show winter-wolf

    "Quando você leva uma tira de carne até a boca e está prestes a mordê-la, você nota uma criatura se aproximando. Você rapidamente pega seu machado, que está encostado ao seu lado, e se prepara para um conflito."

    stranger "Abaixe seu machado, bárbaro."

    hide winter-wolf
    show ravisin
    "Você olha para sua direita, e nota uma figura estranha, olhando você, e equipado com duas adagas de gelo na mão."

    menu:
        "'Quem é você?!'":
            jump pacifier1
            label pacifier1:    
                stranger "Alguém que não quer te matar."

        "Abaixar o machado":
            jump pacifier2
            label pacifier2:
                stranger "Fez bem. Até bárbaros como você podem usar a cabeça de vez em quando."

        "Jamais, estranha! Morra!":
            jump blood_and_gore
            label blood_and_gore:
                stranger "Você fez sua escolha... Rahrz!"
                hide ravisin
                show winter-wolf
                "O lobo feroz avança em seu pescoço antes que você possa tomar qualquer ação ofensiva. Em poucos segundos, você está morto, no chão."
                return
    # This ends the game.

    ravisin "Não se preocupe. Não tenho intenção de te ferir."
    ravisin "Assim como Rahrz"

    hide ravisin
    show winter-wolf
    rahrz "..."

    hide winter-wolf
    show ravisin
    ravisin "Venho propor uma aliança."
    ravisin "Nômades como nós precisamos nos unir se queremos viver mais um dia..."
    ravisin "Eis minha oferta: Uma caravana mercantil passa por uma trilha próxima. Ouvi por ai que alguns orcs planejam uma emboscada na metade do caminho."
    ravisin "Defendemos a caravana e exigimos um pagamento. Um par de braços fortes como os seus são bem-vindos, mas não pense que preciso de você."
    ravisin "E então? O que me diz?"

    return