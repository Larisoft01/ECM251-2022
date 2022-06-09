package Modelos;
public class MobileMembros extends Membros {
    public MobileMembros( String email, String nome, Funcoes funcao) {
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
          System.out.println("Happy Coding!")
          break;
        case Extra :
          System.out.println("Happy_C0d1ng. Maskers");
          break;
    } 
}
}
