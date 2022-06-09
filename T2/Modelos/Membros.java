package Modelos;
package 
public abstract class Membros implements AMostras, BPostarMensagens{
     private String email;
     private String nome;
     private Funcoes funcao;
public Membros(String email, String nome, Funcoes funcao){
    this.email= email;
    this.nome = nome;
    this.funcao = funcao;
}
public String getEmail(){
    return email;
}
public void setEmail(String email){
    this.email = email;
}
public String getNome(){
    return nome;
}
public void setNome(String nome){
    this.nome = nome;
}
public String getFuncao(){
    return funcao;
}
public void setFuncao(String nome){
    this.funcao = funcao;
}
@Override 
public String toString(){
    return "Membro {Nome = " nome", Funcao = " funcao", Email = "email"}";

}
}  
    

