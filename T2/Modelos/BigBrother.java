package Modelos;
package Enum;
package Interface;

    
}

public class BigBrother extends Membros {
    public BigBrother( String email, String nome, Funcoes funcao) {
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
          System.out.println("Sempre
          ajudando as pessoas membros ou não S2! ");
          break;
        case Extra :
          System.out.println("...");
          break;
    } 
}
}