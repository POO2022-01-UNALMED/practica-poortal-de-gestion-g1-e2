package uiMain;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;

import baseDatos.Deserializador;
import baseDatos.Serializador;
import gestorAplicacion.*;
import gestorAplicacion.general.DiaSemana;
import gestorAplicacion.general.Inventario;
import gestorAplicacion.personas.Cliente;
import gestorAplicacion.personas.Contrato;
import gestorAplicacion.personas.Empleado;
import gestorAplicacion.personas.Persona;
import gestorAplicacion.personas.Sexo;
import gestorAplicacion.personas.TipoDocumento;
import gestorAplicacion.ventas.Categoria;
import gestorAplicacion.ventas.Factura;
import gestorAplicacion.ventas.Producto;
import gestorAplicacion.ventas.Servicio;

public class Interfaz {
	private static Scanner sc = new Scanner(System.in);

	private static void guardar() {
		Serializador.serializarTodo();
	}

	private static void cargar() {
		Deserializador.desearilizarTodo();
	}

	private static int readInt() {
		int num = sc.nextInt();
		sc.nextLine();
		return num;
	}

	private static Double readDouble() {
		Double num = sc.nextDouble();
		sc.nextLine();
		return num;
	}

	private static String readString() {
		return sc.nextLine();
	}

	private static LocalDate readDate() {
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
	
	// LOS OBJETOS YA ESTAN GUARDADOS CON EL SERIALIZADOR, DESCOMENTAR EL BLOQUE 
	// Y COMENTAR cargar(); PARA REINICIAR LOS DATOS POR DEFECTO.
	
	/*static {
		// Creacion de servicios
		Servicio s1 = new Servicio("Chef personal", 40000);
		Servicio s2 = new Servicio("Fontanero", 25000);
		Servicio s3 = new Servicio("Estilista", 30000);
		Servicio s4 = new Servicio("Recepcionista", 30000);
		Servicio s5 = new Servicio("Tendero", 30000);
		Servicio s6 = new Servicio("Profesor", 37000);
		Servicio s7 = new Servicio("Entrenador personal", 40000);
		// Creacion de contratos
		Contrato con1 = new Contrato(1200000, LocalDate.of(2022, 5, 1), LocalDate.of(2025, 4, 5));
		Contrato con2 = new Contrato(1300000, LocalDate.of(2022, 4, 21), LocalDate.of(2025, 2, 13));
		Contrato con3 = new Contrato(3300000, LocalDate.of(2020, 5, 23), LocalDate.of(2024, 3, 11));
		Contrato con4 = new Contrato(4200000, LocalDate.of(2022, 3, 15), LocalDate.of(2023, 1, 15));
		Contrato con5 = new Contrato(6000000, LocalDate.of(2021, 11, 8), LocalDate.of(2026, 11, 20));
		// Creacion de clientes
		Cliente c1 = new Cliente("Mateo", "3120201010", "mateo@unal.edu.co", "1234", TipoDocumento.CC, Sexo.MASCULINO);
		Cliente c2 = new Cliente("Alejandro", "3120201010", "alejandro@unal.edu.co", "5678", TipoDocumento.CC,
				Sexo.MASCULINO);
		Cliente c3 = new Cliente("Alejandra", "3120201010", "alejandra@unal.edu.co", "91011", TipoDocumento.TI,
				Sexo.FEMENINO);
		Cliente c4 = new Cliente("Miguel", "3120201010", "miguel@unal.edu.co", "121314", TipoDocumento.CC,
				Sexo.MASCULINO);
		// Creacion de dias de dias laborales
		ArrayList<DiaSemana> dias1 = new ArrayList<DiaSemana>();
		dias1.add(DiaSemana.LUNES);
		dias1.add(DiaSemana.MIERCOLES);
		dias1.add(DiaSemana.VIERNES);
		ArrayList<DiaSemana> dias2 = new ArrayList<DiaSemana>();
		dias2.add(DiaSemana.LUNES);
		dias2.add(DiaSemana.MARTES);
		dias2.add(DiaSemana.MIERCOLES);
		dias2.add(DiaSemana.JUEVES);
		dias2.add(DiaSemana.VIERNES);
		ArrayList<DiaSemana> dias3 = new ArrayList<DiaSemana>();
		dias3.add(DiaSemana.SABADO);
		dias3.add(DiaSemana.DOMINGO);

		Persona p1 = new Persona("Carlos", "32195959", "carlos@email.com", "AY14321541", TipoDocumento.PAP,
				Sexo.MASCULINO);
		Persona p2 = new Persona("Carolina", "314125125", "caro@email.com", "7854125", TipoDocumento.CC, Sexo.FEMENINO);
		Persona p3 = new Persona("Jose", "3141235112", "jose@email.com", "132541231", TipoDocumento.NIP,
				Sexo.MASCULINO);
		Persona p4 = new Persona("Valentina", "3124125412", "valen@email.com", "3542351232", TipoDocumento.CC,
				Sexo.FEMENINO);
		Persona p5 = new Persona("Natalia", "31241235124", "natalia@email.com", "56346326", TipoDocumento.TI,
				Sexo.FEMENINO);

		Empleado e1 = new Empleado("Juan", "3121212111", "juan@email.com", "41412562", TipoDocumento.CC, Sexo.MASCULINO,
				con1, "Supervisor", s1, dias1);
		Empleado e2 = new Empleado("Pepita", "3121937467", "pepita@email.com", "71384549", TipoDocumento.NIP,
				Sexo.FEMENINO, con2, "Supervisor", s3, dias2);
		Empleado e3 = new Empleado("Nicolas", "312851745", "nico@email.com", "248520840", TipoDocumento.CC,
				Sexo.MASCULINO, con3, "Administrador", s2, dias2);
		Empleado e4 = new Empleado("Daniela", "301651852", "daniela@email.com", "152487215", TipoDocumento.CE,
				Sexo.FEMENINO, con4, "Atencion al cliente", s5, dias2);
		Empleado e5 = new Empleado("Samuel", "310165152", "samuel@email.com", "2148965213", TipoDocumento.CE,
				Sexo.MASCULINO, con5, "Atencion al cliente", s6, dias2);

		Producto prod1 = new Producto("PC", 10, Categoria.TECNOLOGIA, 3000000, 24);
		Producto prod2 = new Producto("Audifonos", 30, Categoria.TECNOLOGIA, 100000, 12);
		Producto prod3 = new Producto("Teclado", 16, Categoria.TECNOLOGIA, 140000, 9);
		Producto prod4 = new Producto("Collar", 70, Categoria.MASCOTA, 20000, 6);
		Producto prod5 = new Producto("Pelota", 60, Categoria.MASCOTA, 10000, 3);
		Producto prod6 = new Producto("Vitamina B6", 110, Categoria.SALUD, 12000, 2);
		Producto prod7 = new Producto("Aspirina", 320, Categoria.SALUD, 1500, 1);

	}*/

	public static void main(String[] args) {

		cargar();

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
			case 2:
				gestionarCarrito();
				break;
			case 3:
				devolverProductoInterfaz();
				break;
			case 4:
				seleccionarEmpleadosInterfaz();
				break;
			case 5:
				pagarInterfaz();
				break;
			case 6:
				guardar();
				System.out.println("\n\nVuelve Pronto");
				System.exit(0);
			}

		} while (opcion != 6);
	}

	static void gestionarCarrito() {
		try {
			// Coge los clientes que estan instanciados en ese momento
			ArrayList<Cliente> clientes = Inventario.getClientes();

			System.out.println("\nIngrese el numero del cliente con el que desea realizar el pago\n");
			int opcion;

			// Muestra informacion de los clientes
			for (int i = 0; i < clientes.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + clientes.get(i).mostrarInformacion());
			}

			// Selecciona al cliente
			opcion = (int) readInt() - 1;
			Cliente cliente = clientes.get(opcion);

			// Mientras la persona no ingrese el numero 6, que implica la accion de
			// regresar, este menu va a ser constante
			boolean menu = true;
			while (menu) {
				System.out.println("Elija la opcion que quiere realizar\n");

				System.out.println(" 1. Ver mi carrito");
				System.out.println(" 2. Agregar producto a mi carrito");
				System.out.println(" 3. Agregar servicio a mi carrito");
				System.out.println(" 4. Eliminar producto de mi carrito");
				System.out.println(" 5. Eliminar servicio de mi carrito");
				System.out.println(" 6. Regresar");

				opcion = (int) readInt();

				switch (opcion) {
				case 1:
					System.out.println("\nSu carrito actual esta compuesto por:");
					System.out.println(cliente.verCarrito());
					break;
				case 2:
					productoCarrito(cliente);
					break;
				case 3:
					servicioCarrito(cliente);
					break;
				case 4:
					eliminarProductoCarrito(cliente);
					break;
				case 5:
					eliminarServicioCarrito(cliente);
					break;
				case 6:
					menu = false;
					break;
				}
			}

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}
	}

	static void eliminarServicioCarrito(Cliente cliente) {
		System.out.println("\nPor favor elija un servicio que desee eliminar\n");

		ArrayList<Servicio> servicios;

		// Se verifica que el cliente tenga servicios en el carrito
		try {
			servicios = cliente.getServicios();
		} catch (Throwable e) {
			System.out.println(e.getMessage());
			return;
		}

		// Se muestra informacion de los servicios en el carrito
		for (int i = 0; i < servicios.size(); i++) {
			System.out.println(" " + (i + 1) + ". " + servicios.get(i).getNombre());
		}

		// Selecciona un servicio a eliminar
		int opcion = readInt() - 1;
		Servicio servicio = servicios.get(opcion);
		cliente.eliminarServicioDeLaCanasta(servicio);

		System.out.println("El servicio fue eliminado con exito\n\n");
	}

	static void servicioCarrito(Cliente cliente) {
		System.out.println("Por favor elija un servicio que desee solicitar\n 0. Atras\n");

		// recorre los servicios guardados en el inventario y los imprime
		for (int i = 0; i < Inventario.getServiciosDisponibles().size(); i++) {
			System.out.println(" " + (i + 1) + ". " + Inventario.getServiciosDisponibles().get(i).getNombre());
		}

		// Selecciona una opcion, en caso de que el servicio ya este en el carrito le
		// dice que
		int opcion;
		do {
			try {
				opcion = (int) readInt() - 1;
				if (opcion == -1) {
					break;
				}
				Servicio servicio = Inventario.getServiciosDisponibles().get(opcion);
				cliente.solicitarServicio(servicio);
				System.out.println(
						"El servicio fue solicitado con exito.\nRecuerde que debe asignar un empleado a su servicio antes de realizar el pago\n\n");
				break;
			} catch (Throwable e) {
				System.out.println(e.getMessage());
				System.out.println("Por favor vuelva a ingresar un numero nuevamente\n");
				continue;
			}
		} while (true);
	}

	static void eliminarProductoCarrito(Cliente cliente) {
		System.out.println("\nPor favor elija un producto que desee eliminar\n");

		ArrayList<Producto> productos;

		// Verifica si el cliente tiene productos
		try {
			productos = cliente.getProductos();
		} catch (Throwable e) {
			System.out.println(e.getMessage());
			return;
		}

		// Muestra el nombre de cada producto
		for (int i = 0; i < productos.size(); i++) {
			System.out.println(" " + (i + 1) + ". " + productos.get(i).getNombre());
		}

		// El cliente selecciona un producto y es eleminado del carrito
		int opcion = readInt() - 1;
		Producto producto = productos.get(opcion);
		cliente.eliminarProductoDeLaCanasta(producto);

		System.out.println("El producto fue eliminado con exito\n\n");
	}

	static void productoCarrito(Cliente cliente) {
		System.out.println("Por favor elija un producto que desee agregar a su carrito\n");

		// Se obtiene la lista de productos que tienen una cantidad disponible mayor a 0
		ArrayList<Producto> productoDisp = Inventario.getProductosDisponibles();
		for (int i = 0; i < productoDisp.size(); i++) {
			System.out.println(" " + (i + 1) + ". " + productoDisp.get(i).getNombre() + " Cantidad disponible: "
					+ productoDisp.get(i).getCantidadDisponible() + " unidad(es)");
		}

		// Selecciona un producto
		int opcion = (int) readInt() - 1;
		Producto producto = productoDisp.get(opcion);

		// Si ingresa un numero superior al disponible le pide que ingrese un numero
		// menor
		System.out.println("Ingrese la cantidad a comprar");
		do {
			try {
				int cantidad = (int) readInt();
				if (!producto.verificarCantidad(cantidad)) {
					throw new Error("Por favor ingrese un numero que sea menor a la cantidad disponible\n");
				}

				cliente.agregarProductoALaCanasta(producto, cantidad);
				break;

			} catch (Throwable e) {
				System.out.println(e.getMessage());
				continue;
			}

		} while (true);
	}

	static void pagarInterfaz() {
		try {
			ArrayList<Cliente> clientes = Inventario.clientesConCarrito();
			System.out.println("\nIngrese el numero del cliente con el que desea realizar el pago\n");
			int opcion;

			// Se muestran todos los clientes que no tienen un carrito de compra vacio
			for (int i = 0; i < clientes.size(); i++) {
				System.out.println(" " + (i + 1) + ". " + clientes.get(i).mostrarInformacion());
			}

			// Se elige un cliente
			opcion = (int) readInt() - 1;
			Cliente cliente = clientes.get(opcion);

			// Se realiza la compra
			Factura factura = cliente.pagar();

			// Se muestra la informacion contenida en la factura
			System.out.println("Se ha generado una factura a nombre de " + cliente.getNombre() + " con identificacion "
					+ cliente.getIdentificacion());
			System.out.println(factura.mostrarInformacion());
		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

	static void devolverProductoInterfaz() {
		try {

			System.out.println("\nIngrese el nombre del producto del que desea realizar una devolucion\n");

			String nombreProducto = readString();

			System.out.println("\nIngrese la identificacion del comprador\n");

			String identificacion = readString();

			System.out.println("\nIngrese el numero de productos a realizar devolucion\n");

			int cantidadADevolver = readInt();

			System.out.println("\nIngrese la fecha de la compra en formato DD/MM/YYYY\n");

			LocalDate fecha = readDate();

			String mensaje = Cliente.devolverProducto(nombreProducto, identificacion, cantidadADevolver, fecha);

			System.out.println(mensaje);

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

			// Si ingresa una fecha en la que no hay empleados le pide que la ingrese
			// nuevamente
			ArrayList<Empleado> empleadosDisponibles = new ArrayList<Empleado>();
			do {
				try {
					LocalDate fecha = readDate();
					empleadosDisponibles = servicio.consultarDisponibilidad(fecha);
					if (empleadosDisponibles.size() == 0) {
						throw new Error("No hay empleados disponibles para esta fecha.");
					}
					break;
				} catch (Throwable e) {
					System.out.println(
							"\nNo hay empleados disponibles para ese dia.\nPor favor ingrese la fecha nuevamente\n");
				}
			} while (true);

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
				System.out.println("\nSelecione que accion quiere realizar\n");

				System.out.println(" 1. Contratar persona");
				System.out.println(" 2. Despedir empleado");
				System.out.println(" 3. Visualizar empleados");
				System.out.println(" 4. Atras");

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

	static void despedirInterfaz() {
		try {
			int opcion;

			if (Inventario.getListadoEmpleadosActivos().size() == 0) {
				System.out.println("\nNo hay empleados activos actualmente\n");
				return;
			}
			System.out.println("\nA continuacion, se podra visualizar la lista de empleados:\n");
			for (int i = 1; i <= Inventario.getListadoEmpleadosActivos().size(); i++) {
				System.out.println(
						" " + i + ". " + Inventario.getListadoEmpleadosActivos().get(i - 1).mostrarInformacion());
			}

			System.out.println("\nIngrese el numero de la persona a despedir\n");

			opcion = (int) readInt() - 1;

			Empleado empleadoADespedir = Inventario.getListadoEmpleados().get(opcion);

			empleadoADespedir.despedir();

			System.out.println("\nLa persona " + empleadoADespedir.getNombre() + " con identificacion "
					+ empleadoADespedir.getIdentificacion() + " ha sido despedida de su cargo.\n");

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}
	}

	static void visualizarEmpleadosInterfaz() {
		try {
			for (int i = 1; i <= Inventario.getListadoEmpleados().size(); i++) {
				System.out.println(" " + i + ". " + Inventario.getListadoEmpleados().get(i - 1).mostrarInformacion());
			}
		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}
	}

	static void contratarInterfaz() {
		try {

			int opcion;
			String nuevoCargo;
			String nuevoServicio;
			String nuevosDiasLaborales;
			String nuevoSalario;
			LocalDate fechaRenovacion;
			LocalDate fechaInicio;

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
			if (personasAContratar.size() == 0) {
				System.out.println("\nNo hay actualmente personas disponibles para contratar\n");
				return;
			}
			System.out.println("\nIngrese el numero de la persona a contratar\n");

			for (int i = 1; i <= personasAContratar.size(); i++) {
				System.out.println(" " + i + ". " + personasAContratar.get(i - 1).mostrarInformacion());
			}

			opcion = (int) readInt() - 1;

			Persona personaElegida = personasAContratar.get(opcion);
			// Nuevas contrataciones
			if ((personaElegida instanceof Persona) && !(personaElegida instanceof Empleado)
					&& !(personaElegida instanceof Cliente)) {
				System.out.println(
						"\nA continuacion ingrese el salario que se le asignara al nuevo empleado, su cargo y su fecha final del contrato\n");

				System.out.println("\nIngrese el salario asignado\n");
				nuevoSalario = readString();

				fechaInicio = LocalDate.now();

				System.out.println("\nIngrese la fecha final del contrato en formato DD/MM/YYYY\n");
				LocalDate fechaFin = readDate();

				System.out.println("\nIngrese el cargo asignado\n");
				nuevoCargo = readString();

				System.out.println("\nIngrese el servicio que prestara este empleado: ");
				System.out.println("\nServicios existentes:\n");
				for (Servicio servicio : Inventario.getListadoServicios()) {
					System.out.println(servicio.getNombre());
				}
				nuevoServicio = readString();

				Servicio servicioSeleccionado = Inventario.buscarServicio(nuevoServicio);

				System.out.println("\nDias laborales separados por espacio (ej: LUNES MIERCOLES VIERNES):\n ");
				nuevosDiasLaborales = readString();

				String[] lista = nuevosDiasLaborales.split(" ");
				ArrayList<DiaSemana> diasLaborales = new ArrayList<DiaSemana>();
				for (String i : lista) {
					diasLaborales.add(DiaSemana.valueOf(i.toUpperCase()));
				}

				Contrato contratoPersonaElegida = new Contrato(Integer.parseInt(nuevoSalario), fechaInicio, fechaFin);
				personaElegida.contratar(contratoPersonaElegida, nuevoCargo, servicioSeleccionado, diasLaborales);

				System.out.println("\nLa persona " + personaElegida.getNombre() + " con identificacion "
						+ personaElegida.getIdentificacion() + " ha sido contratada\n");

				// Renovar contrato
			} else {
				System.out.println(
						"\nA continuacion podra visualizar la informacion del empleado recien elegido al cual se le renovara contrato:\n"
								+ "\nSi desea cambiar la informacion, ingresela, sino ingrese 'x'.\n");

				System.out.println("\nCargo: " + ((Empleado) personaElegida).getCargo());
				nuevoCargo = readString();
				

				System.out.println("\nServicio: " + ((Empleado) personaElegida).getServicio().getNombre());
				System.out.println("\nServicios existentes:\n");
				for (Servicio servicio : Inventario.getListadoServicios()) {
					System.out.println(servicio.getNombre());
				}
				nuevoServicio = readString();
				Servicio servicioElegido = null;
				if (!nuevoServicio.equals("x")) {
					servicioElegido = Inventario.buscarServicio(nuevoServicio);
				}

				System.out.println("\nDias laborales separados por espacio (ej: LUNES MIERCOLES VIERNES): "
						+ ((Empleado) personaElegida).getDiasLaborales());
				nuevosDiasLaborales = readString();
				ArrayList<DiaSemana> diasLaborales = new ArrayList<DiaSemana>();
				if (!nuevosDiasLaborales.equals("x")) {
					String[] lista = nuevosDiasLaborales.split(" ");
					for (String i : lista) {
						diasLaborales.add(DiaSemana.valueOf(i.toUpperCase()));
					}
				}

				System.out.println("\nSalario: \n" + ((Empleado) personaElegida).getContrato().getSalario());
				nuevoSalario = readString();
				if (!nuevoSalario.equals("x")) {
					int salario = Integer.parseInt(nuevoSalario);
					((Empleado) personaElegida).getContrato().setSalario(salario);
				}

				System.out.println("\nIngrese la fecha de renovacion de contrato\n");
				fechaRenovacion = readDate();

				((Empleado) personaElegida).renovarContrato(fechaRenovacion);
				
				personaElegida.contratar(null, nuevoCargo, servicioElegido, diasLaborales);
				
				System.out.println("\nEl contrato del empleado ha sido renovado exitosamente.\n");
			}

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

}
