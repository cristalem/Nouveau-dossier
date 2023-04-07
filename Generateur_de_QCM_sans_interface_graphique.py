#Generateur de QCM sans interface graphique
from random import *
import os

"""Utilisation d'une class pour inclure toutes nos fonctions de conversion de base"""
#definition de la class en tant objet de nom : converter
class Conversion_de_base:
    def __init__(self):
        pass

    #flottant a IEEE754
    def decimal_IEEE754(self,x):
        m=0
        e=0
        s=0
        #le signe
        if x>0:
            s='0'
        elif x<0:
            s='1'
            x=str(x)
            x=x.replace('-','')
            x=float(x)

        #l'exposant
        n=1
        a=(x/2**n)
        while a>=2 :
            n=n+1
            a=x/(2**n)
        e=n+127
        e=str(bin(e))
        e=e.replace('0b','')

        #la mantisse
        if a>=1:
            a=a-1
        L=[]
        a=a*2
        while len(L)<23 :
                if a<1:
                    L.append('0')
                    a=a*2
                if a>=1:
                    L.append('1')
                    a=(a-1)*2
                if a==0:
                    L.append('0')
        m=' '.join(L)
        m=m.replace(' ','')
        m=str(m)


        result=s+e+m
        return result

    def IEEE754_decimal(self,x) :
        s=int(x[0])
        e=x[1:9]
        m=x[9:33]
        e=int(e,2)-127
        mi=1.0
        position = 0
        for i in m :
            if m[position] == '1':
                print(position)
                position=position+1
                mi=mi+(1/(2**position))

            else:
                position = position+1
        if s==1:
            s=-1
        else:
            s=1
        print(s,e,mi)
        result=s*mi*(2**e)
        return result

    def binC2universel(self,x):
        len=7
        x=int(x,2)
        if x>=2**7:
            x=x-2**8
            answer=bin(x)
        else:
            answer=bin(x)
        answer=str(answer)
        if answer[0]=='-':
            answer=answer.replace('-0b','')
            answer=answer.zfill(len)
            answer='1'+answer
        elif answer[1]=='b':
            answer=answer.replace('0b','')
            answer=answer.zfill(len)
            answer='0'+answer

        return answer

    def bin_to_base10(self,x):
        a = x
        str=a
        answer = int(str,2)
        return answer

    def base10_to_bin(self,x):
        a = x
        str=a
        answer = int(str,10)
        result = ("{0:{fill}8b}".format(answer, fill='0'))
        result =result.replace("-","1")
        return result

    def base10_to_base16(self,x):

        a = x
        str=a
        answer = int(str,10)
        result =("{0:{fill}0x}".format(answer, fill='0'))
        return result

    def base16_to_base10(self,x):
        a = x
        str=a
        answer = int(str,16)
        return answer

    def bin_to_hexadecimal(self,x):
        a = x
        str=a
        answer = int(str,2)
        result =("{0:{fill}0x}".format(answer, fill='0'))
        return result

    def hexadecimal_to_bin(self,x):
        a = x
        str=a
        answer = int(str,16)
        result = ("{0:{fill}8b}".format(answer, fill='0'))
        return result


    def base_8(self,x):
        a = x
        str=a
        answer = int(str,10)
        result = ("{0:{fill}0o}".format(answer, fill='0'))
        return result
        pass

converter = Conversion_de_base()

""" Creation de nos listes qui vont conetnir toutes les valeurs dont on a besoin"""
#liste qui contient toutes nos questions de conversion
questions_types = ["C2 a Binaire", "binaire à C2", "flottant en IEEE-774", "IEEE-774 a flottant", "Base 10 à binaire", "Binaire a Base 10","Base 10 a Hexadecimal", "Hexadecimal a Base 10","Binaire a Hexadecimal","Hexadecimal a Binaire"]
#liste qui servira de boite a questions en fonction du nombre généré
types_de_questions = []
#nombres qui seront générés aleatoirement
nombre_a_convertir = []
#les nombres générés convertit qui sont autres que les questions
reponse_aux_question = []
# la varible position servira a selectionner le type de question ainsi que sont nombre généré aleatoirement
position = 0
#score qui evoluera en fonction des reponses données par l'utilisateur
score = 0

L_question=[]
L_réponses=[]
L_bonne_reponse=[]
type_QCM=0
"""
Fonction Menu_principal :
Propose a l'utilisateur 2 choix possible :
1 - repondre au QCM
2 - Fabrique des questions
"""
question_exist = 0
def menu_principal():
    try :
        choix_menu_principal = int(input("Que souhaitez vous faire\n 0 : Quitter le programme\n 1 : Repondre aux QCM\n 2 : Fabriquer des questions\n Votre choix : "))
        if choix_menu_principal == 1:
            if question_exist == 1:
                print(type_QCM)
                if type_QCM==0:
                    repondre_QCM()
                elif type_QCM==1:
                    répondre_QCM_Manuel()
            else : 
                print("Veuillez creer des question")
                creer_question()
        elif choix_menu_principal == 0:
            os.system("cls")
            print("Arrêt du programme")
            quit()
        elif choix_menu_principal == 2:
            creer_question()
        else :
            os.system("cls")
            print("entrez un bon choix svp")
            menu_principal()
    except ValueError:
        os.system("cls")
        print("impossible de continuer")
        menu_principal()

"""
Fonction Creer_question :
Propose 3 choix a l'utilisateur :
0 : Retour au menu principal
1 : Generer automatiquement des questions dont il choisit la quantité
2 : Choisit lui meme quel type de conversion veut il ajouter a son QCM
"""
def creer_question():
    
    global nb_question
    global nb_questions_a_generer
    def generation_automatique():
        global type_QCM
        global nb_questions_a_generer
        global question_exist
        type_QCM=0
        nb_questions_a_generer = int(input("Combien de questions voulez vous generer ?\n0 = annuler \nNombre de questions : "))
        os.system("cls")
        if nb_questions_a_generer >= 0 :
            if nb_questions_a_generer == 0:
                print("Vous avez ete redirige vers le menu précedant car vous n'avez pas voulu générer de questions")
                question_exist = 1
                menu_principal()
            for i in range(nb_questions_a_generer):
                types_de_questions.append(randint(0,9)) 
            print("Vos questions ont bien été génére")
            creer_question()
    nb_question = len(types_de_questions)
    try :
        choix = int(input("Que souhaitez vous faire?\n 0 : Retourner au menu principal \n 1 : Générer automatiquement des questions\n 2 : Creer des questions\n Votre choix : "))
        if choix == 1:
            generation_automatique()
        elif choix == 2:
            créer_manuellement()
        elif choix == 0:
            menu_principal()
        else:
            print("entrez un bon choix svp")
            creer_question()
    except ValueError :
        print("impossible de continuer")
        creer_question()


"""
Fonction Repondre au QCM :

- Ensuite va générée des nombres a convertir aleatoirement pour chacune des questions et les mettre dans la liste reponse
  aux questions, pour ensuite les convertir aux choix de conversion demandé,
  Pour chaque question le progreamme génère deux réponses fausse, et impose un choix de 3 réponses différente dont une seule correcte
- Si la reponse est bonne le score change, si c'est le contraire il ne change pas

"""
def repondre_QCM():
    global position
    print(len(types_de_questions))
    #Parmi toutes les questions générées un nombre aleatoire de ses questions sera choisi pour y répondre
    #Pour chacune des questions a repondre, un nombre a convertir aleatoire sera choisi en fonction du type de conversion choisi
    for i in range(len(types_de_questions)):
        if types_de_questions[position]==0 or types_de_questions[position]==1 or types_de_questions[position]==5 or types_de_questions[position]==8:
            tmp_Banswer =  "".join([str(randint(0,1)) for x in range(8)])
            print(tmp_Banswer)
            nombre_a_convertir.append(tmp_Banswer)
        if types_de_questions[position]==2:
            random_float = randint(50,1000)
            random_float = random_float/100
            nombre_a_convertir.append(random_float)
        if types_de_questions[position]==3:
            tmp_IEE774answer =  "".join([str(randint(0,1)) for x in range(32)])
            print(tmp_IEE774answer)
            nombre_a_convertir.append(tmp_IEE774answer)
        if types_de_questions[position]==4 or types_de_questions[position]==6:
            tmp_random_number = randint(-127, 127)
            nombre_a_convertir.append(tmp_random_number)
        if types_de_questions[position]==7 or types_de_questions[position]==9:
            def HexRNG():
                a=randint(1,1000)
                b=hex(a)
                c=int(b,16)
                c=bin(c)
                b=b[2:]
                c=c[2:]
                if len(c)>8:
                    HexRNG()
                if len(c)<8:
                    HexRNG()
                if len(c)==8:
                    print(c)
                    print(b)
                    nombre_a_convertir.append(b)
            HexRNG()
        position = position + 1
    position = 0
    print(nombre_a_convertir)
    #Pour chacune des questions, on génére sa réponse en fonction de son type de conversion
    for x in range(len(types_de_questions)):
        #Conversion de C2 a Bin
        if types_de_questions[position]==0 or types_de_questions[position]==1:
            converted_answer = converter.binC2universel('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)
        #Conversion Decimal a Ieee754
        if types_de_questions[position]==2:
            converted_answer_number = nombre_a_convertir[position]
            converted_answer = converter.decimal_IEEE754(converted_answer_number)
            reponse_aux_question.append(converted_answer)

        #Conversion Decimal a Ieee754
        if types_de_questions[position]==3:
            converted_answer = converter.IEEE754_decimal('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

        #conversion de base10 a Bin
        if types_de_questions[position]==4:
            converted_answer = converter.base10_to_bin('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

        #Conversion de Bin a base 10
        if types_de_questions[position]==5:
            converted_answer = converter.bin_to_base10('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

        #  Conversion de Base 10 a Hexa
        if types_de_questions[position]==6:
            converted_answer = converter.base10_to_base16('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

         # conversion de base 16 a bas10
        if types_de_questions[position]==7:
            converted_answer = converter.base16_to_base10('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

        #conversion de Bin a Hexa
        if types_de_questions[position]==8:
            converted_answer = converter.bin_to_hexadecimal('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)

        #conversion base 16 a bin
        if types_de_questions[position]==9:
            converted_answer = converter.hexadecimal_to_bin('{nombre}'.format(nombre = nombre_a_convertir[position]))
            reponse_aux_question.append(converted_answer)
        position = position +1
    position = -1
    print(reponse_aux_question)
    """
    Fonction repondre :
    Pour chaque question impose 3 reponse differente
    2 fausses est une correcte, et augmente le score si
    la bonne réponse est choisi
    """

    def repondre():
        global position
        global nb_question
        position = position +1
        set_de_reponse = []
        set_de_reponse.append(reponse_aux_question[position])
        real_answer = reponse_aux_question[position]
        # vérifie si la reponse choisie est correcte ou non
        def check_answer(x):
            global score
            # si elle est correcte le score augmente de 1
            if set_de_reponse[x] == real_answer:
                score = score + 1
                print("Bonne reponse votre score augmente de 1 point\nScore actuel : {score_actuel}/{nb_question_total}".format(score_actuel=score,nb_question_total=len(types_de_questions)))
            # Si elle est fause un message mauvaise réponse est affichez
            else :
                print("Mauvaise reponse votre score ne change pas\nScore actuel : {score_actuel}/{nb_question_total}".format(score_actuel=score,nb_question_total=len(types_de_questions)))
        #Génère deux reponse fausse aléatoire en fonction du types de conversion de la question
        for k in range(2):
            if types_de_questions[position]==0 or types_de_questions[position]==1 or types_de_questions[position]==4 or types_de_questions[position]==9:
                tmp_Banswer =  "".join([str(randint(0,1)) for x in range(8)])
                print(tmp_Banswer)
                set_de_reponse.append(tmp_Banswer)
            if types_de_questions[position]==3:
                random_float = randint(50,1000)
                random_float = random_float/100
                set_de_reponse.append(random_float)
            if types_de_questions[position]==2:
                tmp_IEE774answer =  "".join([str(randint(0,1)) for x in range(32)])
                print(tmp_IEE774answer)
                set_de_reponse.append(tmp_IEE774answer)
            if types_de_questions[position]==5 or types_de_questions[position]==7:
                tmp_random_number = randint(-127, 127)
                set_de_reponse.append(tmp_random_number)
            if types_de_questions[position]==6 or types_de_questions[position]==8:
                def HexRNG():
                    a=randint(1,1000)
                    b=hex(a)
                    c=int(b,16)
                    c=bin(c)
                    b=b[2:]
                    c=c[2:]
                    if len(c)>8:
                        HexRNG()
                    if len(c)<8:
                        HexRNG()
                    if len(c)==8:
                        print(c)
                        print(b)
                        set_de_reponse.append(b)
                HexRNG()
        shuffle(set_de_reponse)
        print(set_de_reponse)
        print(real_answer)
        #Demande a l'utilisateur de rentrer un choix de reponse
        if not position > len(types_de_questions):
            global nb_question
            nb_question = nb_question -1
            print("nombre de questions restantes {nb_question}".format(nb_question=nb_question))
            if nb_question == 0:
                def answer_to_questions():
                    try:
                        print("nombre de questions restantes : ", nb_question)
                        answer = int(input("Veuillez entrer la bonne réponse :\n {number}  de {question} :\n 1 : {answer1}\n 2 : {answer2}\n 3 : {answer3}\n Votre réponse : ".format(number=nombre_a_convertir[position], question=len(types_de_questions), answer1=set_de_reponse[0], answer2=set_de_reponse[1], answer3=set_de_reponse[2])))
                        if answer == 1 or answer ==2 or answer==3:
                            check_answer(answer-1)
                        else : 
                            print("choix incorrect, veuillez en entrer un valide")
                    except ValueError:
                        print("Choix incorrect entrez un choix de réponse correct")
                        answer_to_questions()
                answer_to_questions()
                print("Félicitation, vous avez répondu a toutes les questions.\n Votre score finale est de {score}".format(score=score))
                def retry():
                    try : 
                        continuer = int(input("Voulez vous :\n 1 : Retourner au menu principal\n 2 : Quitter le programme "))
                        if continuer == 1:
                            menu_principal()
                        if continuer == 2:
                            quit()
                        else :
                            print("Choix incorect") 
                            retry()
                    except ValueError:
                        print("impossible de continuer")
                retry()
            else:
                def answer_to_questions():
                    try:
                        print("nombre de questions restantes : ", nb_question)
                        answer = int(input("Veuillez entrer la bonne réponse :\n {number}  de {question} :\n 1 : {answer1}\n 2 : {answer2}\n 3 : {answer3}\n Votre réponse : ".format(number=nombre_a_convertir[position], question=len(types_de_questions), answer1=set_de_reponse[0], answer2=set_de_reponse[1], answer3=set_de_reponse[2])))
                        if answer == 1 or answer ==2 or answer==3:
                            check_answer(answer-1)
                            repondre()
                        else : 
                            print("choix incorrect, veuillez en entrer un valide")
                    except ValueError:
                        print("Choix incorrect entrez un choix de réponse correct")
                        answer_to_questions()
                    repondre()
                answer_to_questions()
                    
    repondre()
"""la fonction "créer manuellement" permet a l'utilisateur de créer ses propres questions de lui-même
en choisissant la question posée, les réponses possibles, et la bonne réponse."""
def créer_manuellement():
    global type_QCM
    global question_exist
    type_QCM=1
    
    try :
        n=int(input('ATTENTION vous devrez créer tout le QCM vous même de A à Z.\ncombien de questions voulez vous créer ?\n 0 : Annuler\n>>>'))
        if n ==0:
            print('annulation')
            menu_principal()
    except ValueError :
        print('veuillez mettre un nombre entier.')
        créer_manuellement()
    for i in range (1,n+1):
        question=input('quelle est votre question ?\n>>>')
        L_question.append(question)

        reponse1=input(f'question {i}\n1ère réponse possible ?\n>>>')
        while reponse1=='':
            reponse1=input(f'question {i}\n1ère réponse possible ?\n>>>')

        reponse2=input(f'question {i}\n2e réponse possible ?\n>>>')
        while reponse2=='':
            reponse2=input(f'question {i}\n2e réponse possible ?\n>>>')

        reponse3=input(f'question {i}\n3e réponse possible ?\n>>>')
        while reponse3=='':
            reponse3=input(f'question {i}\n3e réponse possible ?\n>>>')

        L_réponses.append([reponse1, reponse2, reponse3])

        bonne_reponse=int(input(f'question {i}\nquelle est la bonne réponse parmi ces trois la ?\n1 : {reponse1}\n2 : {reponse2}\n3 : {reponse3}\n>>>'))
        while bonne_reponse<1 or bonne_reponse>3 :
            print('Choisissez une des trois reponses entrés précédemment !')
            bonne_reponse=int(input(f'question {i}\nquelle est la bonne réponse parmi ces trois la ?\n1 : {reponse1}\n2 : {reponse2}\n3 : {reponse3}\n>>>'))
        bonne_reponse==L_réponses[i-1][bonne_reponse-1]
        print('question créée !')
        L_bonne_reponse.append(bonne_reponse)
        question_exist = 1
        menu_principal()

"""La fonction "répondre QCM Manuel" permet au code d'interprêter 
et afficher les questions crées par l'utilisateur a l'aide de la fonction 
"créer manuellement". """

def répondre_QCM_Manuel():
    score=0
    for i in range(len(L_question)):
        print('il reste ', len(L_question)-(i+1),' questions.')
        answer=0
        while answer<1 or answer>3 :
            print('choisissez une réponse proposée')
            answer=int(input(f'{L_question[i]}\n1 : {L_réponses[i][0]}\n2 : {L_réponses[i][1]}\n3 : {L_réponses[i][2]}\n>>>'))
        index_bonne_réponse=int(L_bonne_reponse.index(L_bonne_reponse[i])+1)
        print(index_bonne_réponse)
        if answer==index_bonne_réponse:
            score+=1
            print("Bonne réponse ! votre score augmente d'un point !")
            print(score)
        else :
            print(f'mauvaise réponse ! la bonne réponse était {L_bonne_reponse[i]}.')
            print(score)
    print(f"fin du QCM ! Votre score final est de {score}")
    menu_principal()


menu_principal()
