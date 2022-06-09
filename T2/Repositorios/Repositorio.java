package Repositorios;
import java.util.ArrayList;
import Modelos.Membros;
import Repositorios.ARepositorio;

public class Repositorio implements ARepositorio {
    private ArrayList<Membros> listeMembros = new ArrayList<Membros>();

}
@Override

public ArrayList<Membros> getMembros(){
    return listeMembros;
}

@Override

public void addMembro(Membro membro){
  this.listeMembros.add(membro);
}

@Override 

public void removerMembro(Membro membro){
    this.listeMembros.remove(membro);
  }

