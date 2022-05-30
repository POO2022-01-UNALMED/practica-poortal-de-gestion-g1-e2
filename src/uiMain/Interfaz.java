package uiMain;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Arrays;

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
				con1, "Cajero", s2, diasE1);
		Empleado e2 = new Empleado("Pepita", "35555", "pepita@pepita.com", "123514", TipoDocumento.CC, Sexo.FEMENINO,
				con2, "Manicurista", s3, diasE2);

		Producto prod1 = new Producto("PC", 10, Categoria.TECNOLOGIA, 10000, 10);

		// c1.solicitarServicio(s3);
		// c1.solicitarServicio(s2);
		c1.agregarProductoALaCanasta(prod1, 7);
	}

	public static void main(String[] args) {

		// cargar(); Liberar cuando ya este todo hecho

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
				// guardar(); Liberar cuando ya este todo hecho
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
		System.out.println("Por favor elija un servicio que desee solicitar\n0 para regresar\n");

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
				break;
			} catch (Throwable e) {
				System.out.println(e.getMessage());
				System.out.println("Por favor vuelva a ingresar un numero nuevamente\n");
				continue;
			}
		} while (true);

		System.out.println(
				"El servicio fue solicitado con exito.\nRecuerde que debe asignar un empleado a su servicio antes de realizar el pago\n\n");
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

		System.out.println("El servicio fue eliminado con exito\n\n");
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
		System.out.println("ingrese la cantidad a comprar");
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

			System.out.println("\nIngrese el nombre del producto del que desea realizar una devolución\n");

			String nombreProducto = readString();

			System.out.println("\nIngrese la identificación del comprador\n");

			String identificacion = readString();

			System.out.println("\nIngrese el número de productos a realizar devolución\n");

			int cantidadADevolver = readInt();

			System.out.println("\nIngrese la fecha de la compra en formato DD/MM/AAAA\n");

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
				System.out.println("Selecione que accion quiere realizar\n");

				System.out.println(" 1. Contratar persona");
				System.out.println(" 2. Despedir empleado");
				System.out.println(" 3. Visualizar empleados");
				System.out.println(" 4. Atrás");

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

			System.out.println("\nA continuación, se podrá visualizar la lista de empleados:\n");

			for(int i = 1; i < Inventario.getListadoEmpleados().size();i++ ){
				System.out.println(" "+i+". "+Inventario.getListadoEmpleados().get(i-1).mostrarInformacion());
			}

			System.out.println("\nIngrese el número de la persona a despedir\n");

			opcion = (int) readInt() - 1;

			Empleado empleadoADespedir = Inventario.getListadoEmpleados().get(opcion);

			empleadoADespedir.despedir();

			System.out.println("\nLa persona "+empleadoADespedir.getNombre()+" con identificación "+empleadoADespedir.getIdentificacion()+" ha sido despedida de su cargo.\n");

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}
	}

	static void visualizarEmpleadosInterfaz() {
		try {
			for(int i = 1; i <= Inventario.getListadoEmpleados().size();i++ ){
				System.out.println(" "+i+". "+Inventario.getListadoEmpleados().get(i-1).mostrarInformacion());
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

			for (int i = 1; i <= personasAContratar.size(); i++) {
				System.out.println(" "+i + ". " + personasAContratar.get(i - 1).mostrarInformacion());
			}
			
			System.out.println("\nIngrese el numero de la persona a contratar\n");

			opcion = (int) readInt() - 1;

			Persona personaElegida = personasAContratar.get(opcion);

			if((personaElegida instanceof Persona) && !(personaElegida instanceof Empleado) && !(personaElegida instanceof Cliente) ){
				System.out.println("\nA continuación ingrese el salario que se le asignará al nuevo empleado, su cargo y su fecha final del contrato\n");
				
				System.out.println("\nIngrese el salario asignado\n");
				nuevoSalario = readString();
				int salario = Integer.parseInt(nuevoSalario);
                
				LocalDate fechaFin = LocalDate.now();

				System.out.println("\nIngrese la fecha final del contrato\n");
				fechaInicio =  readDate();

				Contrato contratoPersonaElegida = new Contrato(salario,fechaInicio, fechaFin);

				System.out.println("\nLa persona" + personaElegida.getNombre() + "con identificación "+personaElegida.getIdentificacion()+" ha sido contratada\n");
				
			}else{
				System.out.println("\nA continuación podrá visualizar la información del empleado recién elegido al cual se le renovará contrato:\n"
				+ "\nSi desea cambiar la información, ingrésela, sino ingrese 'x'.\n"	);		

				System.out.println("\nCargo: \n"+ ((Empleado)personaElegida).getCargo());
				nuevoCargo = readString();
				if(nuevoCargo != "x"){
					((Empleado)personaElegida).setCargo(nuevoCargo);
				}

				System.out.println("\nServicio: \n"+ ((Empleado)personaElegida).getServicio().getNombre());
				nuevoServicio = readString();
				if(nuevoServicio != "x"){
					((Empleado)personaElegida).getServicio().setNombre(nuevoServicio);
				}

				System.out.println("\nDías laborales separados por coma (ej: lunes, miercoles): \n"+ ((Empleado)personaElegida).getDiasLaborales());
				nuevosDiasLaborales = readString(); 
				if(nuevosDiasLaborales != "x"){
					String[] lista = nuevosDiasLaborales.split(",");
                	ArrayList<String> diasLaborales = new ArrayList<String>(Arrays.asList(lista));
 					((Empleado)personaElegida).setDiasLaborales(diasLaborales);
				}

				System.out.println("\nSalario: \n"+ ((Empleado)personaElegida).getContrato().getSalario());
				nuevoSalario = readString();
				if(nuevoSalario != "x"){
					int salario = Integer.parseInt(nuevoSalario);
					((Empleado)personaElegida).getContrato().setSalario(salario);
				}

                System.out.println("\nIngrese la fecha de renovación de contrato\n");
				fechaRenovacion =  readDate();

				((Empleado)personaElegida).renovarContrato(fechaRenovacion);

			}			

		} catch (Throwable e) {
			System.out.println(e.getMessage());
		}

	}

}
