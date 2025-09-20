import java.util.Arrays;

public class EjerArreglos {

    private int[][] ventas = new int[3][12];

    public EjerArreglos() {
    }

    public void insertarVenta(int departamento, int mes, int valor) {
        if (departamento >= 0 && departamento < ventas.length && mes >= 0 && mes < ventas[0].length) {
            ventas[departamento][mes] = valor;
            System.out.println("Venta agregada con éxito.");
        } else {
            System.out.println("Los índices de departamento o mes no son válidos.");
        }
    }

    public void buscarVenta(int valorBuscado) {
        boolean encontrado = false;
        System.out.print("Se encontraron ventas con el valor " + valorBuscado + " en las siguientes ubicaciones: ");
        for (int i = 0; i < ventas.length; i++) {
            for (int j = 0; j < ventas[i].length; j++) {
                if (ventas[i][j] == valorBuscado) {
                    System.out.print("[" + i + ", " + j + "] ");
                    encontrado = true;
                }
            }
        }
        if (!encontrado) {
            System.out.print("No se encontró ninguna venta con ese valor.");
        }
        System.out.println();
    }

    public void eliminarVenta(int departamento, int mes) {
        if (departamento >= 0 && departamento < ventas.length && mes >= 0 && mes < ventas[0].length) {
            ventas[departamento][mes] = 0;
            System.out.println("Venta eliminada exitosamente.");
        } else {
            System.out.println("Los índices de departamento o mes no son válidos.");
        }
    }

    public void imprimirVentas() {
        System.out.println("\n--- Estado actual de las ventas ---");
        String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
        for (int i = 0; i < ventas.length; i++) {
            System.out.print(departamentos[i] + ": ");
            System.out.println(Arrays.toString(ventas[i]));
        }
        System.out.println("-----------------------------------");
    }

    public static void main(String[] args) {
        EjerArreglos gestor = new EjerArreglos();

        gestor.insertarVenta(0, 0, 500);
        gestor.insertarVenta(1, 5, 1200);
        gestor.insertarVenta(2, 11, 800);
        gestor.imprimirVentas();

        gestor.buscarVenta(1200);
        gestor.buscarVenta(999);

        gestor.eliminarVenta(0, 0);
        gestor.imprimirVentas();
    }
}