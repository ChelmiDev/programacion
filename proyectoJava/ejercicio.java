public class ejercicio{
    public static void main(String[] args) {
        // SE LLAMA LA FUNCION SUMAR
        int resultado = sumar(5, 8, 6);
        System.out.println("La suma de las tres parametros son: " + resultado);

        // SE LLAMA LA CLASE COCHE
        Coche coche = new Coche();
        coche.Puertas();
        coche.Puertas();
        coche.Puertas();
        System.out.println("Numeros de puertas: " + coche.numeroPuertas);
    }

    // SE CREA LA FUNCION SUMAR
    public static int sumar(int a, int b, int c) {
        return a + b + c;
    }
}

// SE CREA LA CLASE COCHE  
class Coche{
    int numeroPuertas = 0;

    public void Puertas(){
         this.numeroPuertas++;
        }
    }
