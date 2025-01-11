"""Levels definition.

Explicación dificultad de los niveles:

La idea es que en algunos casos sea difícil porque el hechizo es largo, y en otros casos
tiene que ser dificil porque el tiempo es poco.

En los primeros niveles, tiene que ser fácil segun ambos parámetros, y en los últimos
difíciles también los dos.

Anoté entonces los largos de cada hechizo (que estan buenísimos, no los cambiemos) y le
asigné un tiempo total en función de el tipo de dificultad y el nro de nivel. A partir de
eso calculo la velocidad (tiempo por letra).

  level name        chars  time  speed  score  description
  ---------------   -----  ----  -----  -----  -----------
  Teatro prestado     45    35    0.77     58   Es el más facil, la intro
  Opera               57    27    0.47    121   Mas difícil, pero no tanto
  Magic arena        102    50    0.49    208   Muy largo, tiempo que le alcance
  Fiesta musical     117    48    0.41    285   Más largo, menos tiempo
  Las Vegas          134    48    0.36    372   Más largo, tiempo apretado
  Black magic        119    40    0.34    350   Menos letras, pero cae más el tiempo
  Tatooine           114    35    0.31    367   Sigue acortandose, menos tiempo
  Area 51            113    30    0.27    418   Igual de largo, bastante menos tiempo
  Graveyard          134    25    0.19    705   Mas largo, el tiempo es aun menor
  El lugar feliz     145    20    0.14   1036   Mas complicado que la mierda

  Max score is determined by the difficulty of the level (roughly quantity of chars / speed).
"""

import os

from typuspocus.i18n import tr
from typuspocus.people import Wardrobe, all_wardrobes

AUDIENCIA = os.path.join(os.path.dirname(os.path.realpath(__file__)), "audiencia")


textosNiveles = [
    (
        tr("Lousy Pub"),
        [Wardrobe(AUDIENCIA + '/girl/', 'articles0.txt'),
         Wardrobe(AUDIENCIA + '/boy/', 'articles0.txt')],
        "conejo2",     # conejo
        "hocus pocus, disappear now, desaparecelo chico.",
        tr(
            "Cast the spell as fast and accurately as you can.\n"
            "You can backspace and fix your mistakes."),
        tr(
            "Great!\n"
            "You receive an offer to perform in the Paris Opera."),
        tr("You are not even worthy of this demo level."),
        dict(tiempo_por_caracter=0.77, preferencia_precision=0.5, max_score=58)
    ),
    (
        tr("Paris Opera"),
        # Gente vestida bien
        [Wardrobe(AUDIENCIA + '/fashion_girl/', 'articles1.txt', "fullydressed"),
         Wardrobe(AUDIENCIA + '/boy/', 'articles1.txt', "fullydressed")],
        "mask",  # La mascara del fantasma de la opera
        "evanesco simulatio, phantasma spectaculum. initium capere.",
        tr("Disappear the Phantom's mask, that will embarrass him and make him leave."),
        tr(
            "Your act was great!\n"
            "You are invited to perform the Halftime show at the local basquetball finals."),
        tr(
            "You blew it, your father disinherited you.\n"
            "You get a job coding ruby on rails."),
        dict(tiempo_por_caracter=0.47, preferencia_precision=0.5, max_score=121)
    ),
    (
        tr("Magic Arena"),
        all_wardrobes,  # Jugadores de basquet o deportistas,
        "zapatillas",  # Zapatillas grandes
        (
            "luckyus calceus sneakerus, evanesco consagrus, valius playerus, "
            "propugnator turma championus."
        ),
        tr("The locals are loosing by 12, you must disappear the visitor's MVP lucky sneakers."),
        tr(
            "Thanks to your help the locals win and you get invited to do your trick at "
            "the after party."),
        tr("An Angry mob of the local fans chases you around the stadium."),
        dict(tiempo_por_caracter=0.49, preferencia_precision=0.5, max_score=208)
    ),
    (
        tr("Goth Party"),
        # Hip-hoperos o darkies
        [Wardrobe(AUDIENCIA + '/goth/', 'articles3.txt', "gothdressed")],
        "vicios",  # Alcohol, drogas, hacer un mix
        (
            "sexus drugus rockanrolus, captivus crowdimus yowasaaap. cops and hardcopy "
            "marihuanus boozelion, cocuchus chuchu fuchu."
        ),
        tr(
            "You were supposed to disappear a Milli Vanilli CD, instead you must vanish the "
            "drugs to hide them from the cops."),
        tr(
            "You got away clean, and kept a lot of famous people out of jail.\n"
            "You are going to Las Vegas now!!"),
        tr("You go to jail charged with drug possession."),
        dict(tiempo_por_caracter=0.41, preferencia_precision=0.5, max_score=285)
    ),
    (
        "Las Vegas",
        all_wardrobes,  # Gente adinerada
        "docs",  # papeles y documentos
        (
            "factus taxus nulus, nilun actin, evaDus fiscus IRSus, whySaw "
            "Elvis Bellagium 11 ocean's cardus impustum disapiros ipsofactum."
        ),
        tr(
            "You get to Las Vegas to perform in a Casino, but the owners want to take advantage "
            "of your power to evade taxes."),
        tr(
            "The IRS wants you for beeing an accesory to tax evasion.\n"
            "They send you Africa where they'll never find you."),
        tr("Your act was a total failure, you got wasted and lost all your money playing craps."),
        dict(tiempo_por_caracter=0.36, preferencia_precision=0.5, max_score=372)
    ),
    (
        tr("Black Magic"),
        # Africanitos de la tribu
        [Wardrobe(AUDIENCIA + '/girl/', 'articles5.txt', "fullydressed"),
         Wardrobe(AUDIENCIA + '/boy/', 'articles5.txt', "fullydressed")],
        "mucielago",  # Un muricélago, o algún animal raro
        (
            "Batsimus chicaka aFrIcuN triBuson, ill chikakun medicor, nigrum. comedo. "
            "crudus...pain cooking Shutlewor meellon cHuNgo."
        ),
        tr(
            "You go to live with a tribe in africa, they find out you are a wizard and want "
            "you to heal their ill sacred animal."),
        tr(
            "You disappeared the sacred animal.  The angry natives start chasing you around "
            "the jungle."),
        tr("The natives made a tasty casserole out of you."),
        dict(tiempo_por_caracter=0.34, preferencia_precision=0.5, max_score=350)
    ),
    (
        "Tatooine",
        [Wardrobe(AUDIENCIA + '/boy/', 'articles6.txt', "enmascarados")],
        "aspiradora",  # Aspiradora loca
        (
            "Arturitum Vacuumcleanerum Ev4niscum c3p0 venusiun rescusum grossum ph1ll1ps, "
            "disapirum spacious robotitus shakulus."
        ),
        tr(
            "While running away from the natives, a spaceship abducts you. The Venusians ask "
            "you to help them vanish a hitchhiker."),
        tr(
            "Since you were so helpful, the Venusians send you back to Earth in an "
            "individual spaceship."),
        tr(
            "Because you were unwilling to cooperate, the Venusians performed crazy "
            "things with a light saber on your body."),
        dict(tiempo_por_caracter=0.31, preferencia_precision=0.5, max_score=367)
    ),
    (
        tr("Area 51"),
        [Wardrobe(AUDIENCIA + '/boy/', 'articles_alien.txt', "alien_alien"),
         Wardrobe(AUDIENCIA + '/boy/', 'articles_mib.txt', "alien_mib")],
        "alien",  # un marcianito de roswell
        (
            "Marcianus 51area alf rosswellin didosong untilyourestingherewithme evanisum "
            "marcianus y guarda que viene molderrr."
        ),
        tr(
            "Your ship was running a pirated OS and crashed in New Mexico. The FBI captures "
            "you and asks you to disappear some evidence of the alien landings."),
        tr(
            "Now that the evidence exists only on your memory, the FBI makes sure you "
            "won't talk by putting a cap in your head."),
        tr(
            "You couldn't do it.  But you'll have a lot of time to practice since you are "
            "never leaving Area 51."),
        dict(tiempo_por_caracter=0.27, preferencia_precision=0.5, max_score=418)
    ),

    (
        tr("Graveyard"),
        [Wardrobe(AUDIENCIA + '/boy/', 'articles8.txt', "esqueletos")],
        "anubis",  # Estatuilla de Anubis
        (
            "vaderetrum satinus anubisun chungus, transformix this decayed form to "
            "Mumm-ra the Everliving and the puwur of christus will savius vox."
        ),
        tr(
            "Ok, you died, and went to hell, you can escape to heaven by disappearing Anubis.\n"
            "All the dead gather around to watch..."),
        tr(
            "You did it!!! Now you go to heaven, that happy place we all dream about as "
            "kids, that place where men and women love each other."),
        tr(
            "You stay in hell. At least you won't have problems finding a lawyer if you ever "
            "come to need one."),
        dict(tiempo_por_caracter=0.19, preferencia_precision=0.5, max_score=705)
    ),
    (
        tr("Hugh's Place"),
        # Todos desnudos,
        [Wardrobe(AUDIENCIA + '/fashion_girl/', 'articles9.txt', "enpelotas"),
         Wardrobe(AUDIENCIA + '/boy/', 'articles9.txt', "enpelotas")],
        "cabra",  # CUZCO la cabra
        (
            "caelum CUZCUS 13 paradisiun, revivisco animalis playboyus housus, pornus sexus "
            "gross klunx workus my clunk essta noshi inbolus minusem. miau miau."
        ),
        tr(
            "Here we are, it's beautiful, everything that disappears here goes back to Earth, "
            "so you are going to revive a lovely goat now!"),
        tr(
            "Congratulations!\n"
            "You fullfilled your destiny as a Magician!"),
        tr(
            "Mmm...\n"
            "Too bad you couldn't do it, but hey, a horde of naked angels offers to console you!"),
        dict(tiempo_por_caracter=0.14, preferencia_precision=0.5, max_score=1036)
    ),
]


class Niveles:
    def __init__(self, keys, values):
        for k, v in zip(keys, values):
            setattr(self, k, v)


keys = """
nombre
audiencia
objeto
hechizo
historyintro
historygood
historybad
params
""".strip().split("\n")
niveles = [Niveles(keys, values) for values in textosNiveles]

if __name__ == "__main__":
    for n in niveles:
        print("\n" + n.nombre)
        print("   ", repr(n.historyintro))
        print("   ", repr(n.historygood))
        print("   ", repr(n.historybad))
