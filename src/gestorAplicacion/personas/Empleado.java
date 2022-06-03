package gestorAplicacion.personas;

import java.time.LocalDate;
import java.util.ArrayList;

import gestorAplicacion.general.DiaSemana;
import gestorAplicacion.general.Inventario;
import gestorAplicacion.ventas.Servicio;

/**
 * Esta clase extiende de persona y se encarga de manejar los empleados de la aplicacion
 * los cuales se usan para atender a los servicios, la creacion de facturas y manejar su 
 * proceso de contratacion.
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 */
public class Empleado extends Persona {
	private static final long serialVersionUID = 1L;

	private Contrato contrato;
	private String cargo;
	private Servicio servicio;
	private ArrayList<DiaSemana> diasLaborales = new ArrayList<DiaSemana>();

	/**
	 * Este constructor se usa para la construccion generica desde 0 de los empleados, es decir,
	 * cuando no existe una persona previamente relacionada.
	 * 
	 * @param nombre
	 * @param telefono
	 * @param email
	 * @param identificacion
	 * @param tipoDeIdentificacion
	 * @param sexo
	 * @param contrato
	 * @param cargo
	 * @param servicio
	 * @param diasLaborales
	 */
	public Empleado(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo, Contrato contrato, String cargo, Servicio servicio,
			ArrayList<DiaSemana> diasLaborales) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
		this.contrato = contrato;
		this.cargo = cargo;
		this.servicio = servicio;
		this.diasLaborales = diasLaborales;

	}

	/**
	 * Este constructor se usa para la contratacion para cuando se crea un empleado
	 * a partir de una persona ya existente. En este se elimina la persona que existia previamente
	 * ya que por el comportamiento de la herencia, quedaria la persona duplicada. De igual manera,
	 * como no hay nada asociado a la persona, no hay problema con la consistencia de datos.
	 * 
	 * @param persona
	 * @param contrato
	 * @param cargo
	 * @param servicio
	 * @param diasLaborales
	 */
	public Empleado(Persona persona, Contrato contrato, String cargo, Servicio servicio,
			ArrayList<DiaSemana> diasLaborales) {
		super(persona.nombre, persona.telefono, persona.email, persona.identificacion, persona.tipoDeIdentificacion,
				persona.sexo);
		Inventario.eliminarPersona(persona);
		this.contrato = contrato;
		this.cargo = cargo;
		this.servicio = servicio;
		this.diasLaborales = diasLaborales;

	}

	public Contrato getContrato() {
		return contrato;
	}

	public void setContrato(Contrato contrato) {
		this.contrato = contrato;
	}

	public String getCargo() {
		return cargo;
	}

	public void setCargo(String cargo) {
		this.cargo = cargo;
	}

	public Servicio getServicio() {
		return servicio;
	}

	public void setServicio(Servicio servicio) {
		this.servicio = servicio;
	}

	public ArrayList<DiaSemana> getDiasLaborales() {
		return diasLaborales;
	}

	public void setDiasLaborales(ArrayList<DiaSemana> diasLaborales) {
		this.diasLaborales = diasLaborales;
	}

	/**
	 * Verifica que el empleado que este activo, es decir, tenga un contrato vigente. Adicionalmente
	 * verifica si esta disponible en el dia solicitado, esto se hace segun el dia de la semana correspondiente.
	 * 
	 * @param servicio
	 * @param fechaSolicitud
	 * @return disponible
	 */
	public boolean consultarDisponibilidadEmpleado(Servicio servicio, LocalDate fechaSolicitud) {
		boolean disponible = false;
		if (this.servicio == servicio && this.isActivo(fechaSolicitud)) {
			for (DiaSemana i : diasLaborales) {
				if (i.ordinalDia - 1 == (fechaSolicitud.getDayOfWeek().ordinal())) {
					disponible = true;
				}
			}
		}
		return disponible;
	}

	/**
	 * Consulta si el contrato esta vigente actualmente
	 * @return boolean
	 */
	public boolean isActivo() {
		return contrato.consultarVigencia(LocalDate.now());
	}
	
	/**
	 * Consulta si el contrato esta vigente en la fecha especificada
	 * @return boolean
	 */
	public boolean isActivo(LocalDate fecha) {
		return contrato.consultarVigencia(fecha);
	}
	
	
	/**
	 * Devuelve un texto con informacion del empleado dependiendo si tiene contrato vigente o no.
	 * @return informacion
	 */
	public String mostrarInformacion() {
		String informacion = "";
		if (this.isActivo()) {
			informacion = "Soy el empleado con contrato vigente " + nombre + " con numero de identificacion: "
					+ identificacion;
		} else {
			informacion = "Soy el empleado sin contrato vigente " + nombre + " con numero de identificacion: "
					+ identificacion;
		}
		return informacion;
	}

	/**
	 * Establece el dia actual como fecha final del contrato para realizar su despido
	 */
	public void despedir() {
		LocalDate hoy = LocalDate.now();
		this.contrato.setFechaFin(hoy);
	}
	/**
	 * Establece una nueva fecha fin del contrato para alargar su vigencia
	 */
	public void renovarContrato(LocalDate fechaFin) {
		if (fechaFin.isAfter(contrato.getFechaFin())) {
			this.contrato.setFechaFin(fechaFin);
		}

	}
}
