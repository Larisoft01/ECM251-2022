package Repositorios;

import java.util.ArrayList;
import Modelos.Membros;

public interface ARepositorio {
    void addMembro(Membros membro);
    void removerMembro(Membros membro);
    ArrayList<Membros> getMembros();
    
}
