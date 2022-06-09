package Modelos;

public class ScriptGuys extends Membros {
    public ScriptGuys( String email, String nome, Funcoes funcao) {
        super (email, nome, funcao);
    }
@Override

public void mostrar() {
    System.out.println(toString());
}

@Override 

public void mensagem(Horarios horario){
    switch (horario) {
        case OK :
          System.out.println(" Prazer em ajudar novos amigos de Código!");
          break;
        case NOOK :
          System.out.println(" QU3Ro_S3us_r3curs0s.py ");
          break;
    } 
}
}
