Trabalho Echo Server - Gerenciador de chaves

Echo server "Key manager" que utiliza a classe Cofre e User onde
são armazenados, checados o nível de suas senhas utilizando regex 
com seus dados e informações dos cofres, e salvados suas informações
num file json para ser acessado depois.
O cliente manuseia uma cópia do seu cofre e o servidor tem acesso e manuseia 
realmente os dados de todos os usuários.