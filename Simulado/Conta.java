// Larissa Navarro Pizarro 19.02028-7

public class Conta {
    private int valor;
    private double saldo;
    
// Construtor

    public Conta (Usuário usuario, int valor){
        this.valor = valor;
        this.cliente = cliente;
        saldo = 0;
    }

// Método 
    public String versaldo(){
        return String.format("R$.2f", saldo);
         
    }
    public boolean depositar(double valor){
        if(valor < 0)
           return false;
        this.saldo += valor;
        return true;
    }
    public boolean transferirDinheiro(double valor. Conta destino){
        if(!destino.depositar(valor)) return false;
        return true;
    
    }
    public String toString(){
        return "Conta Numero:" + id +
        "\n Saldo:" + visualizarSaldo() +
        "\n Cliente:" + cliente.getNome();

    }
    
}
