<!doctype html> <!-- Salvar como gravarPet.php -->
<html lang="pt-br">
	<head>
		<title>Gravação de Pet</title>
		<meta charset="UTF-8">
	</head>
	<body>
	<?php
		/*
			Exemplos - Explicação de matrizes
		$nome = "Ana Clara" ; // sou uma variável
		
		$idades[0] = 15;
		$idades[1] = 97;
		$idades[2] = 42;
		$idades[3] = 22;
		
		$populacao["Sao Paulo"] = 22971102;
		$populacao["Rio de Janeiro"] = 14970200;
		$populacao["Santa Catarina"] = 8750191;
		
		echo " A cidade de São Paulo tem " . $populacao["Sao Paulo"] ;
		*/
		
		// 1 - Receber os dados do formulário
		// Dependendo do método usado no formulário, os 
		// dados chegam na matriz $_GET[] ou $_POST[]
		
		// Vou criar uma variável para cada elemento
		// que está chegando do formulário
		$nome 				= $_POST["nome"] ;
		$tipo				= $_POST["tipo"] ;
		$sexo 				= $_POST["sexo"] ;
		$dono				= $_POST["dono"] ;
		
		// checkbox podem gerar problemas se não estiverem
		// checados / ticados - Resolvendo isto... 
		
		// Criando a variável com valor padrão
		$vacinado=0;
		
		// se o objetivo veio, atualizo a variável
		if(isset($_POST["vacinado"]))
		{
			$vacinado= $_POST["vacinado"] ;
		}
		
		$peso 				= $_POST["peso"] ;
		$idade 				= $_POST["idade"] ;
		$ultimaConsulta 	= $_POST["ultimaConsulta"] ;
		$prontuario 		= $_POST["prontuario"] ;
		
		// Os arquivos chegam na matriz $_FILES[]
		$foto 		= $_FILES["foto"]["name"] ;
		$tamanho	= $_FILES["foto"]["size"] ;
		$tipoArquivo= $_FILES["foto"]["type"] ;
		$nomeTmp  	= $_FILES["foto"]["tmp_name"] ;
		
		// Dados de arquivos vêm na matriz $_FILES[]
		// 2 - Validação básica (nome em branco?, etc.)
		// Nome do pet não pode ficar em branco
		if ($nome==""){
			die("Nome do pet não pode ficar vazio");
		}
		
		// Tipo do pet não pode ficar vazio
		if ($tipo == "") {
			die("Tipo do pet deve ser escolhido!");
		}
		
		// Peso não pode ser negativo 
		// Peso não pode ser maior que 99.999
		if ( ($peso < 0) OR ($peso >99.999) )
		{
			die("O peso deve estar entre 0 e 99.999 !");
		}
		
		// Idade não pode ser menor que 0 (negativo)
		// Idade não pode ser maior que 99
		if (($idade <0) OR ($idade>99))
		{
			die("Idade deve estar entre 0 e 99.");
		}	

		// 3 - Mostrar dados recebidos na tela
		echo "<h1>Gravando Pet...</h1>";
		echo "O nome do pet é $nome <br>" ;

		echo "Tipo: $tipo <br>" ;
		echo "Sexo: $sexo <br>" ;
		echo "Dono: $dono <br>" ;
		echo "Vacinado: $vacinado <br>" ;
		echo "Peso: $peso <br>" ;
		echo "Idade: $idade <br>" ;
		echo "Última Consulta: $ultimaConsulta <br>" ;
		echo "Prontuário: <br> $prontuario <hr>" ;
		echo "<h2>Arquivo</h2>";
		echo "Nome: $foto <br>";
		echo "Tamanho: $tamanho	bytes <br>";
		echo "Tipo: $tipoArquivo <br>";
		echo "Nome Temporário: $nomeTmp";
		
		// 4 - Conectar no servidor MYSQL
		$con = mysqli_connect("localhost", "root", "");
		
		// 5 - Enviar comando SQL de inclusão p/ MYSQL
		
		// 6 - Mostrar na tela que Pet foi inserido
	?>
	</body>
</html>