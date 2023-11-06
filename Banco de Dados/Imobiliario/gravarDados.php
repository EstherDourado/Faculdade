<!doctype html>
<html lang="pt-br">
    <head>
        <title>Cadastro Imobiliario</title>
    </head>
    <body>
        <?php

            $nome           = $_POST["nome"];
            $telefone       = $_POST["telefone"];
            $email          = $_POST["email"]
            $tipoImovel     = $_POST["tipo"];
            $numeroRegistro = $_POST["numeroEscritura"];
            $localRegistro  = $_POST["localEscritura"]; //erro 
            $operacao       = $_POST["operacao"];
            

            $foto1 		= $_FILES["foto1"]["name"] ;
            $tamanho	= $_FILES["foto1"]["size"] ;
            $tipoArquivo= $_FILES["foto1"]["type"] ;
            $nomeTmp  	= $_FILES["foto1"]["tmp_name"];
            
            $foto2 		= $_FILES["foto2"]["name"] ;
            $tamanho	= $_FILES["foto2"]["size"] ;
            $tipoArquivo= $_FILES["foto2"]["type"] ;
            $nomeTmp  	= $_FILES["foto2"]["tmp_name"]; 

            $dataEscritura  = $_POST["data"];
            $valor          = $_POST["valor"];
            $desocupado     = 0;
            $descricao      = $_POST["descriçao"];

            if(isset($_POST["Idesocupado"])){
			    $vacinado= $_POST["Idesocupado"];
		    }

            if ($nome == ""){
                die("Campo nome não pode ficar vazio");
            }

            if($email == ""){
                die("Campo nome não pode ficar vazio");
            }
        
            if ($numeroRegistro == ""){
                die("Campo número do registo não pode ficar vazio");
            }

            if ($localRegistro == ""){
                die("Campo local do registro não pode ficar vazio");
            }

            if ($tipoImovel == ""){
                die("O tipo do imovel deve ser escolhido");
            }
            
            if ($valor < 0){
                die("Valor invalido, o valor precisa ser maior que 0");
            }
            
            echo "Nome: Esther Dourado Batista<br>RGM: 30038693";
            echo "<h1> Os seguintes dados serão gravados</h1>";
            echo "Seu nome: $nome <br>";
            echo "Seu telefone: $telefone <br>";
            echo "Seu email: $email <br>";
            echo "O tipo do imovel: $tipoImovel <br>";
            echo "O número do registro da escritura: $numeroRegistro <br>";
            echo "O local do registro da escritura: $localRegistro <br>";
            echo "O tipo de operação: $operacao <br>";
            echo "$foto1 <br>";
            echo "$foto2 <br>";
            echo "A data da escritura é $dataEscritura <br>";
            echo "O valor do imovel é $valor <br>";
            echo "O imovel está: $desocupado <br>";
            echo "Descrição do imovel: $descricao <br>";

            $con = mysqli_connect("localhost", "root", "");

            mysqli_set_charset($con,"utf8");

            mysqli_select_db($con, "ESTHER30038693") or
                die("Erro na abertura do banco de dados:" .
                    mysqli_error($con));   

            $sql="INSERT INTO CADASTRO(
                            nome,
                            telefone,
                            email
                            tipoImovel,
                            numeroEscritura,
                            localEscritura,
                            tipoOperaçao,
                            imovelDesocupado,
                            dataEscritura,
                            valor,
                            foto1,
                            foto2,
                            descrição)
            VALUES      (
                            '$nome',
                            '$telefone',
                            '$email',
                            '$tipoImovel',
                            '$numeroRegistro',
                            '$localRegistro',
                            '$operacao',
                            '$desocupado',
                            '$dataEscritura',
                            '$valor',
                            '$foto1',
                            '$foto2',
                            '$descricao')
            ";

            mysqli_query($con, $sql) or 
            die(
                "Erro na inserção do formulario imobiliario:<br>" .
                mysqli_error($con)
            );

            if ($foto1 <> ""){
                $destino = "arquivo\\$foto1";
                echo "Movendo arquivo de  $nomeTmp para $destino";

                move_uploaded_file($nomeTmp, $destino) or 
                die("Falha na transferência do arquivo:" .
                    $_FILES["foto1"]["error"]);

            echo "<br> <img src='$destino' width='150'> <br>";
            }

            if ($foto2 <> ""){
                $destino2 = "arquivo\\$foto2";
                echo "<br>Movendo arquivo de $nomeTmp para $destino2";
            
                move_uploaded_file($nomeTmp, $destino2) or 
                die("<br>Falha na transferência do arquivo:" .
                    $_FILES["foto2"]["error"]);

            echo "<br> <img src='$destino2' width='150'> <br>";
            }

            echo "<br>$nome seu cadastro está finalizado!<hr>";
        ?>
    </body>
</html>