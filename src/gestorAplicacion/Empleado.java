package gestorAplicacion;

import java.time.LocalDate;
import java.util.ArrayList;

public class Empleado extends Persona {
	private Contrato contrato;
	private String cargo;
	private String departamento;
	private Servicio servicio;
	private ArrayList<String> diasLaborales = new ArrayList<String>();

	public Empleado(String nombre, String telefono, String email, String identificacion,
			TipoDocumento tipoDeIdentificacion, Sexo sexo, Contrato contrato, String cargo, String departamento,
			Servicio servicio) {
		super(nombre, telefono, email, identificacion, tipoDeIdentificacion, sexo);
		this.contrato = contrato;
		this.cargo = cargo;
		this.departamento = departamento;
		this.servicio = servicio;
	}

    public void despedir(){

    }

	public void renovarContrato(LocalDate fechaFin){

	}

	public void contratarPersona(Persona persona, int salario, LocalDate fechaFin, Servicio servicio){

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

	public String getDepartamento() {
		return departamento;
	}

	public void setDepartamento(String departamento) {
		this.departamento = departamento;
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

	public boolean consultarDisponibilidadEmpleado(Servicio servicio, LocalDate fechaSolicitud){
        boolean a = false;
		if(this.servicio == servicio){
            for(String i: diasLaborales){
				if(i == (fechaSolicitud.getDayOfWeek().toString())){
					a = true;
				}
			}
		}return a;
	}

}
