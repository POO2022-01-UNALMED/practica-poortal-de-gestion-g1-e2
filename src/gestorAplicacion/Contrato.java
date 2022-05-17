package gestorAplicacion;

import java.time.LocalDate;
import static java.time.temporal.ChronoUnit.DAYS;

public class Contrato extends Documento {
	private String identificador;
	private int salario;
	private LocalDate fechaInicio;
	private LocalDate fechaFin;

	public Contrato(int salario, LocalDate fechaInicio, LocalDate fechaFin) {
		super();
		this.salario = salario;
		this.fechaInicio = fechaInicio;
		this.fechaFin = fechaFin;
		this.identificador = generarIdentificador();
	}

	public boolean consultarVigencia(Contrato contrato) {
		LocalDate hoy = LocalDate.now();
		return hoy.isAfter(fechaFin);
	}

	public LocalDate getFechaInicio() {
		return fechaInicio;
	}

	public void setFechaInicio(LocalDate fechaInicio) {
		this.fechaInicio = fechaInicio;
	}

	public LocalDate getFechaFin() {
		return fechaFin;
	}

	public void setFechaFin(LocalDate fechaFin) {
		this.fechaFin = fechaFin;
	}

	public String getIdentificador() {
		return identificador;
	}

	public int getSalario() {
		return salario;
	}

	public void setSalario(int salario) {
		this.salario = salario;
	}

	String generarIdentificador() {
		String text = "";
		for (int i = 0; i < 5; i++) {
			text += ((int) (Math.random() * 10)) + "";
		}
		return text;
	}
	
	public long cantidadDiasEmpresa() {
		return DAYS.between(LocalDate.now(), fechaInicio);
		
	}
}
