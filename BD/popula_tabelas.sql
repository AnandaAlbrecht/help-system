truncate table helpsystem.TB_USER;
insert into helpsystem.TB_USER(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO)
values('joao', 'Joao Santos', 'joao@gmail.com', 'joao1234', CURDATE());
  
insert into helpsystem.TB_USER(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO)
values('marcos', 'Marcos Abel', 'marcos@gmail.com', 'marcos1234', CURDATE());

insert into helpsystem.TB_USER(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO)
values('vitor', 'Vitor Eleo', 'vitor@gmail.com', 'vitor1234', CURDATE());
  
insert into helpsystem.TB_USER(STR_USER, STR_NOME_PESSOA, STR_EMAIL, STR_SENHA, DT_ULTIMA_ALTERACAO)
values('marcia', 'Marcia Oi', 'marcia@gmail.com', 'marcia1234', CURDATE());

select * from `helpsystem`.`TB_USER` ;

insert into helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA)
values(6, 'Normalmente, quantos litros de sangue uma pessoa tem? Em média, quantos são retirados numa doação de sangue?',  'a) Tem entre 2 a 4 litros. São retirados 450 mililitros
b) Tem entre 4 a 6 litros. São retirados 450 mililitros
c) Tem 10 litros. São retirados 2 litros
d) Tem 7 litros. São retirados 1,5 litros
e) Tem 0,5 litros. São retirados 0,5 litros', null, CURDATE());

insert into helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA)
values(6, 'De quem é a famosa frase “Penso, logo existo”?',  
'a) Platão
b) Galileu Galilei
c) Descartes
d) Sócrates
e) Francis Bacon', 
null, CURDATE());

insert into helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA)
values(7, 'De onde é a invenção do chuveiro elétrico?',  
'a) França
b) Inglaterra
c) Brasil
d) Austrália
e) Itália', 
null, CURDATE());

insert into helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA)
values(8, 'Quais o menor e o maior país do mundo?',  
'a) Vaticano e Rússia
b) Nauru e China
c) Mônaco e Canadá
d) Malta e Estados Unidos
e) São Marino e Índia', 
null, CURDATE());

insert into helpsystem.TB_PERGUNTAS(ID_USER, STR_TITULO, STR_PERGUNTA, FLAG_RESOLVIDO, DT_PERGUNTA)
values(9, 'Qual o nome do presidente do Brasil que ficou conhecido como Jango?',  
'a) Jânio Quadros
b) Jacinto Anjos
c) Getúlio Vargas
d) João Figueiredo
e) João Goulart', 
null, CURDATE());

select * from helpsystem.TB_PERGUNTAS;

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(1, 7, true, 'Tem entre 4 a 6 litros. São retirados 450 mililitros', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(1, 8, false, 'c) Tem 10 litros. São retirados 2 litros', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(1, 9, false, 'e) Tem 0,5 litros. São retirados 0,5 litros', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(2, 6, false, 'a) Platão', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(2, 7, false, 'd) Sócrates', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(2, 8, true, 'c) Descartes', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(2, 9, false, 'e) Francis Bacon', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(2, 6, false, 'b) Galileu Galilei', CURDATE());



insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(3, 6, false, 'a) França', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(3, 7, false, 'b) Inglaterra', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(3, 8, true, 'c) Brasil', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(3, 9, false, 'd) Austrália', CURDATE());

insert into helpsystem.TB_RESPOSTAS(ID_PERGUNTA, ID_USER, FLAG_MELHOR_RESPOSTA, STR_RESPOSTA, DT_RESPOSTA)
values(3, 6, false, 'e) Itália', CURDATE());

select * from helpsystem.TB_RESPOSTAS;

