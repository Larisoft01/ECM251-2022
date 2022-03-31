public class App {
    public void run(){
        Cliente cliente = new Cliente("Dawn", "1000", "poketrainer@gmail.com");
        Conta conta = new Conta(cliente, 1234);
        System.out.println(conta);
    }
}
    
}
