package gestorAplicacion;

import java.time.LocalDate;
import java.util.ArrayList;

public class Empleado extends Persona {
	private Contrato contrato;
	private String cargo;
	private Servicio servicio;
	private ArrayList<String> diasLaborales = new ArrayList<String>();

	public Empleado(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo, Contrato contrato, String cargo, String departamento,
			Servicio servicio) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
		this.contrato = contrato;
		this.cargo = cargo;
		this.servicio = servicio;
		Inventario.agregarEmpleado(this);
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

	public ArrayList<String> getDiasLaborales() {
		return diasLaborales;
	}

	public void setDiasLaborales(ArrayList<String> diasLaborales) {
		this.diasLaborales = diasLaborales;
	}

	public boolean consultarDisponibilidadEmpleado(Servicio servicio, LocalDate fechaSolicitud) {
		boolean disponible = false;
		if (this.servicio == servicio) {
			for (String i : diasLaborales) {
				if (i == (fechaSolicitud.getDayOfWeek().toString())) {
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
		return "Soy " + nombre + " con numero de identificacion: " + identificacion;
	}
	public void despedir() {
		LocalDate hoy = LocalDate.now();
		contrato.setFechaFin(hoy);	
	}

	public void renovarContrato(LocalDate fechaFin) {
		if (fechaFin.isAfter(contrato.getFechaFin())){
            contrato.setFechaFin(fechaFin);
		}    
	}
}

