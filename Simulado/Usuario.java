public class Usuario {
    private String nome;
    private String senha;
    private String email;

    public Usuario (String nome, String email){
        this.nome = nome;
        this.email = email;
    }

    

    private Usuario (String senha){
        this.senha= senha;
    }

    public void run(){
        Usuario usuario = new usuario("Dawn", "10000", "poketrainer@gmail.com");
        Conta conta = new Conta(usuario, 2001);
        System.out.println(conta);
    }

    public void verUsuario(){
        System.out.println("Dados do Cliente:");
        System.out.println("Nome:" + nome);
        System.out.println("E-mail:" + email);
    }
    public String getNome(){
        return nome;

    }
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }
    

    
}
