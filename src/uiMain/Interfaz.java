package uiMain;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.*;

public class Interfaz {
	static Scanner sc = new Scanner(System.in);

	private static void guardar() {
		Serializador.serializarTodo();
	}

	private static void cargar() {
		Deserializador.desearilizarTodo();
	}

	static int readInt() {
		int num = sc.nextInt();
		sc.nextLine();
		return num;
	}

	static Double readDouble() {
		Double num = sc.nextDouble();
		sc.nextLine();
		return num;
	}

	static String readString() {
		return sc.nextLine();
	}

	static LocalDate readDate() {

		String dateString;

		do {
			try {
				dateString = sc.nextLine();
				if (!dateString.matches("\\d{2}/\\d{2}/\\d{4}")) {
					throw new Error("Formato de fecha ingresado es invalido.");
				}
				String[] dateParts = dateString.split("/");
				return LocalDate.of(Integer.parseInt(dateParts[2]), Integer.parseInt(dateParts[1]),
						Integer.parseInt(dateParts[0]));
			} catch (Throwable e) {
				System.out.println("Formato o fecha invalida. Intente nuevamente");

				continue;
			}
		} while (true);

	}

	// Objetos a crear
	static {
		Servicio s1 = new Servicio("Chef personal", 40000);
		Servicio s2 = new Servicio("Fontanero", 25000);
		Servicio s3 = new Servicio("Estilista", 30000);

		Contrato con1 = new Contrato(1200000, LocalDate.of(2022, 5, 15), LocalDate.of(2023, 5, 15));
		Contrato con2 = new Contrato(1300000, LocalDate.of(2022, 5, 15), LocalDate.of(2024, 5, 15));

		Cliente c1 = new Cliente("Mateo", "3120201010", "malvarezle@unal.edu.co", "1234", TipoDocumento.CC,
				Sexo.MASCULINO);
		ArrayList<DiaSemana> diasE1 = new ArrayList<DiaSemana>();
		diasE1.add(DiaSemana.LUNES);
		diasE1.add(DiaSemana.MIERCOLES);
		diasE1.add(DiaSemana.VIERNES);
		ArrayList<DiaSemana> diasE2 = new ArrayList<DiaSemana>(2);
		diasE2.add(DiaSemana.LUNES);
		diasE2.add(DiaSemana.MARTES);
		diasE2.add(DiaSemana.MIERCOLES);
		diasE2.add(DiaSemana.JUEVES);
		diasE2.add(DiaSemana.VIERNES);
		Empleado e1 = new Empleado("Juan", "3121212111", "juan@juan.com", "41412562", TipoDocumento.CC, Sexo.MASCULINO,
				con1, "Cajero", null, diasE1);
		Empleado e2 = new Empleado("Pepita", "35555", "pepita@pepita.com", "123514", TipoDocumento.CC, Sexo.FEMENINO,
				con2, "Manicurista", s3, diasE2);

		c1.solicitarServicio(s3);
	}

	public static void main(String[] args) {

		// cargar(); Liberar cuando ya est� todo hecho

		System.out.println(Inventario.getListadoPersonas());
		System.out.println(Inventario.getListadoFacturas());

		System.out.println("Buenos dias Administrador\n\n");

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
			case 1:
				gestionarEmpleadosInterfaz();
				break;
			case 4:
				seleccionarEmpleadosInterfaz();
				break;
			case 5:
				pagarInterfaz();
				break;
			case 6:
				// guardar(); Liberar cuando ya est� todo hecho
				System.out.println("\n\nVuelve Pronto");
				System.exit(0);
			}

		} while (opcion != 6);
	}

	static void contratarInterfaz() {
		try {

			int opcion;

			ArrayList<Persona> personasAContratar = new ArrayList<Persona>();
			for (Empleado empleado : Inventario.getListadoEmpleados()) {
				if (empleado.isActivo() == false) {
					personasAContratar.add(empleado);
				}
			}
			for (Persona persona : Inventario.getListadoPersonas()) {
				if ((persona instanceof Persona) && !(persona instanceof Empleado) && !(persona instanceof Cliente)) {
					personasAContratar.add(persona);
				}
			}
			mostrarPersonasAContratar(personasAContratar);

			System.out.println("\nIngrese el numero de la persona a contratar\n");

			opcion = (int) readInt() - 1;

			Persona personaElegida = personasAContratar.get(opcion);

			contratar(personaElegida, personaElegida.cargo, personaElegida.servicio );

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

	static String mostrarPersonasAContratar(ArrayList<Persona> personasAContratar) {
		String listaPersonasAContratar = "";
		for (int i = 1; i <= personasAContratar.size(); i++) {
			listaPersonasAContratar = i + ". " + personasAContratar.get(i - 1).mostrarInformacion();
		}
		return listaPersonasAContratar;
	}

	static void pagarInterfaz() {
		try {
			ArrayList<Cliente> clientes = Inventario.clientesConCarrito();

			System.out.println("\nIngrese el numero del cliente con el que desea realizar el pago\n");
			int opcion;

			for (int i = 0; i < clientes.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + clientes.get(i).mostrarInformacion());
			}
			opcion = (int) readInt() - 1;
			Cliente cliente = clientes.get(opcion);
			Factura factura = cliente.pagar();

			System.out.println("Se ha generado una factura a nombre de " + cliente.getNombre() + " con identificacion "
					+ cliente.getIdentificacion());
			System.out.println(factura.mostrarInformacion());
		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

	static void seleccionarEmpleadosInterfaz() {
		try {
			ArrayList<Cliente> clientes = Inventario.clientesConCarrito();

			System.out.println("\nIngrese el numero del cliente con el que desea seleccionar empleados\n");
			int opcion;

			for (int i = 0; i < clientes.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + clientes.get(i).mostrarInformacion());
			}
			opcion = (int) readInt() - 1;
			Cliente cliente = clientes.get(opcion);
			ArrayList<Servicio> servicios = cliente.obtenerServiciosSinEmpleado();

			System.out.println("\nIngrese el numero del servicio del cual desea seleccionar un empleado\n");

			for (int i = 0; i < servicios.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + servicios.get(i).toString());
			}
			opcion = (int) readInt() - 1;
			Servicio servicio = servicios.get(opcion);

			System.out.println("\nIngrese la fecha en la cual desea recibir su servicio en formato DD/MM/YYYY");

			LocalDate fecha = readDate();

			ArrayList<Empleado> empleadosDisponibles = servicio.consultarDisponibilidad(fecha);

			if (empleadosDisponibles.size() == 0) {
				throw new Error("No hay empleados disponibles para esta fecha.");
			}

			System.out.println("\nIngrese el numero del empleado con el que desea recibir su servicio\n");

			for (int i = 0; i < empleadosDisponibles.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + empleadosDisponibles.get(i).mostrarInformacion());
			}

			opcion = (int) readInt() - 1;

			Empleado empleadoSeleccionado = empleadosDisponibles.get(opcion);

			cliente.seleccionarEmpleado(servicio, empleadoSeleccionado);
			System.out.println("Se ha asignado el empleado " + empleadoSeleccionado.getNombre() + " al servicio "
					+ servicio.getNombre());

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

	static void gestionarEmpleadosInterfaz() {
		try {
			int opcion;
			do {
				System.out.println("Selecione que accion quiere realizar\n");

				System.out.println(" 1. Contratar persona");
				System.out.println(" 2. Despedir empleado");
				System.out.println(" 3. Visualizar empleados");
				System.out.println(" 4. Atr�s");

				opcion = readInt();

				switch (opcion) {
				case 1:
					contratarInterfaz();
					break;
				case 2:
					despedirInterfaz();
					break;
				case 3:
					visualizarEmpleadosInterfaz();
					break;
				}

			} while (opcion != 4);
		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

}
