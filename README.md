# Othello

C'est un jeu Othello programmé en Python dans le cadre d'un projet tutoré.

Le jeu se lance en demandant via une boîte de dialogue la taille de la grille souhaité au joueur. Il a le choix entre une grille 4x4, 6x6 ou 8x8.
Une fois la taille sélectionnée, la grille du jeu s'affiche dans le terminal et le premier joueur peut commencer à jouer.

Pour saisir un mouvement, le joueur saisit deux caractères : 
  - le premier est une lettre minuscule et indique le numéro de ligne ( a pour la première ligne, b pour la deuxième, etc...),
  - le deuxième est le numéro de colonnes (en commençant par 1).
Par exemple, si le joueur souhaite poser un pion sur la première ligne et la première colonne, il doit saisir a1 . Si le mouvement n'est pas valide,
la saisie sera répétée jusqu'à la saisie d'un mouvement valide ou la demande d'accès au menu principal.

Le tour du premier ou du deuxième joueur est indiqué dans le terminal.

Pour accéder au menu principal du jeu, le joueur peut saisir 'M' en pleine partie. Une boîte de dialogue s'affiche alors pour 
demander au joueur quel action il souhaite exécuter. Il a le choix entre 5 actions : 
  - 0 pour terminer le jeu,
  - 1 pour commencer une nouvelle partie,
  - 2 pour charger une partie,
  - 3 pour sauvegarder une partie (si une partie est en cours),
  - 4 pour reprendre la partie (si une partie est en cours).
  
Lorsque qu'un joueur a plus de pions que l'autre, la partie se termine et le joueur gagnant est affiché.
 
