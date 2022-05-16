package uiMain;

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
			
			System.out.println("Gestionar Empleados");
			System.out.println("Gestionar Carrito");
			System.out.println("Devolver Producto");
			System.out.println("Elegir empleados para servicios seleccionados");
			System.out.println("Pagar");
			System.out.println("Guardar y cerrar");
			
			opcion = readInt();
			
			switch (opcion) {
			
			}
			
		} while (opcion != 6);
	}
	
}
