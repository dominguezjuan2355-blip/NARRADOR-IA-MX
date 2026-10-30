import random

COMENTARIOS = {
    "gol": {
        "narrador_1": [
            "¡GOOOOOOL! ¡La mandó a guardar!",
            "¡Qué definición! ¡Imparable!",
            "¡Se viene abajo el estadio! ¡Golazo!"
        ],
        "narrador_2": [
            "La defensa estaba de espectadora, ¡qué barbaridad!",
            "¡Al portero le dejaron una tarea imposible!",
            "¡Y luego preguntan por qué se emocionan los aficionados!"
        ]
    },
    "atajada": {
        "narrador_1": [
            "¡QUÉ ATAJADÓN! ¡Voló para salvar a su equipo!",
            "¡El portero acaba de hacer una parada espectacular!",
            "¡Le negó el gol con una intervención tremenda!"
        ],
        "narrador_2": [
            "¡Manos de acero! ¡Qué reflejos!",
            "Ese portero acaba de ganarse los aplausos.",
            "¡La defensa ya le debe una cena!"
        ]
    },
    "fallo": {
        "narrador_1": [
            "¡No puede ser! ¡Era una oportunidad clarísima!",
            "¡La tuvo, la tuvo y la dejó escapar!",
            "¡Qué ocasión se acaba de perder!"
        ],
        "narrador_2": [
            "¡Eso era más difícil fallarlo que marcarlo!",
            "El balón todavía está buscando dónde cayó.",
            "¡La afición no se puede creer lo que acaba de pasar!"
        ]
    },
    "penal": {
        "narrador_1": [
            "¡PENAL! ¡Se señala desde los once pasos!",
            "¡Atención, que puede cambiar el partido!",
            "¡Toda la presión está sobre el cobrador!"
        ],
        "narrador_2": [
            "Aquí se necesita sangre fría y mucha precisión.",
            "¡El portero tendrá que adivinar el destino del balón!",
            "¡Momento de máxima tensión!"
        ]
    }
}

def narrar(evento):
    evento = evento.strip().lower()

    if evento not in COMENTARIOS:
        print("Evento desconocido. Usa: gol, atajada, fallo o penal.")
        return

    frases = COMENTARIOS[evento]

    print("\n🎙️ NARRADOR 1:")
    print(random.choice(frases["narrador_1"]))

    print("\n🎙️ NARRADOR 2:")
    print(random.choice(frases["narrador_2"]))

if __name__ == "__main__":
    print("⚽ NARRADOR IA MX")
    print("Eventos: gol, atajada, fallo, penal")
    while True:
        evento = input("\n¿Qué ocurrió? (o escribe salir): ")
        if evento.strip().lower() == "salir":
            break
        narrar(evento)
