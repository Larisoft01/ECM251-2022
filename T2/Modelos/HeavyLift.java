package Modelos;
import Enum.Horarios;;

public class HeavyLift extends Membros {
    public HeavyLift (String email, String nome, Funcoes funcao){
        super (email, nome, funcao);
    
    }
@Override

public void mostrar(){
    System.out.println(toString());

}


@Override

public void mensagem(Horarios horario){
    switch (horario) {
        case OK :
          System.out.println( "Podem contar conosco!");
          break;
        case Extra :
          System.out.println("N00b_qu3_n_Se_r3pita.bat");
          break;
    } 
}
}
