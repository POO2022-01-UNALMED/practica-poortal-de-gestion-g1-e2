package gestorAplicacion;

import java.time.LocalDate;
import java.util.ArrayList;

public class Empleado extends Persona {
	private Contrato contrato;
	private String cargo;
	private Servicio servicio;
	private ArrayList<DiaSemana> diasLaborales = new ArrayList<DiaSemana>();

	public Empleado(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo, Contrato contrato, String cargo,
			Servicio servicio, ArrayList<DiaSemana> diasLaborales) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
		this.contrato = contrato;
		this.cargo = cargo;
		this.servicio = servicio;
		this.diasLaborales = diasLaborales;
	}

	public void despedir() {

	}

	public void renovarContrato(LocalDate fechaFin) {

	}

	public void contratarPersona(Persona persona, int salario, LocalDate fechaFin, Servicio servicio) {

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

	public boolean consultarDisponibilidadEmpleado(Servicio servicio, LocalDate fechaSolicitud) {
		boolean disponible = false;
		if (this.servicio == servicio) {
			for (DiaSemana i : diasLaborales) {
				if (i.ordinalDia == (fechaSolicitud.getDayOfWeek().ordinal())) {
					disponible = true;
				}
			}
		}
		return disponible;
	}

	public boolean isActivo() {
		return contrato.consultarVigencia();
	}
	
	public String mostrarInformacion() {
		String informacion = "";
		if(this.isActivo()){
		    informacion = "Soy el empleado sin contrato vigente" + nombre + " con numero de identificacion: " + identificacion;
		}else{
			informacion = "Soy el empleado con contrato vigente" + nombre + " con numero de identificacion: " + identificacion;
		}
		return informacion;
	}

}
