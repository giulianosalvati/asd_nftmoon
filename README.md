# Dice Game :game_die: - Project B
"Architetture dei Sistemi Distribuiti" course project  @ UniCampus Rome - Developed by Marco Salmè, Daniele Mercuri, Giuliano Salvati e Massimo Capurro LlAdo'.

# Exam Task :page_facing_up:
> Tramite l’utilizzo di REMIX, GANACHE, META-MASK e WEB3; implementare un sistema di gioco basato su token ERC-20 e ERC-721 che funzioni nel seguente modo: 
  il giocatore possiede un account metamask che utilizza per ”registrarsi” al gioco.
  L’implementazione del gioco viene lasciata libera puo andare da un semplice lancio di dadi, o una partita di carte in stile black-jack fino ad un effettiva partita di scacchi contro il pc o altro.
  Durante il log-in viene controllato se all’account sono intestati degli ERC-721 e in caso affermativo viene sbloccato il contenuto esclusivo associato all’ERC-721 nel gioco. Ex: un dado esclusivo.
  Alla fine della partita vengono attribuiti degli ERC-20 all’address del giocatore in base al punteggio effettuato.
  In questo modo nel contratto dell’ERC-20 si andrà a generare una classifica dei giocatori. E’ possibile instanziare come metadata dell’ERC-721 anche solo un codice che risolto al di fuori della blockchain porti a sbloccare il collezionabile e non il collezionabile stesso.
  Tramite i token ERC-20 vinti con le varie partite è possibile comprare i token ERC-721.

# How to get started:
 ## Before the execution
   1. Setting Ganache Local Blockchain
   
      :pushpin: Remember to leave Ganache open while code running.
   2. Setting Brownie with Ganache

 ## To execute the game

  > brownie run main.py
 
