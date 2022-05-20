package uiMain;

import java.util.ArrayList;
import java.util.Scanner;

import gestorAplicacion.*;

public class Interfaz {
	static Scanner sc = new Scanner(System.in);

	static int readInt() {
		return sc.nextInt();
	}

	static Double readDouble() {
		return sc.nextDouble();
	}

	static String readString() {
		return sc.nextLine();
	}

	public static void main(String[] args) {
		System.out.println("Buenos días Administrador\n\n");

		int opcion;

		do {
			System.out.println("Selecione que accion quiere realizar\n");

			System.out.println(" 1. Gestionar Empleados");
			System.out.println(" 2. Gestionar Carrito");
			System.out.println(" 3. Devolver Producto");
			System.out.println(" 4. Elegir empleados para servicios seleccionados");
			System.out.println(" 5. Pagar");
			System.out.println(" 6. Guardar y cerrar");

			opcion = readInt();

			switch (opcion) {
			case 5:
				pagarInterfaz();
				break;
			}

		} while (opcion != 6);
	}

	static void pagarInterfaz() {
		ArrayList<Cliente> clientes = Inventario.clientesConCarrito();

		if (clientes.isEmpty()) {
			System.out.println("No hay clientes con servicios o productos en su carrito de compra");
		}

		int opcion;

		for (Cliente i : clientes) {
			System.out.println(" 1. " + i.mostrarInformacion());
		}

		opcion = readInt() - 1;

		Cliente cliente = clientes.get(opcion);
		Factura factura = cliente.pagar();

		System.out.println("Se ha generado una factura a nombre de " + cliente.getNombre() + " con identificacion "
				+ cliente.getIdentificacion());
		System.out.println(factura.mostrarInformacion());
	}

}
