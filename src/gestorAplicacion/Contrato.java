package gestorAplicacion;

import java.time.LocalDate;
import static java.time.temporal.ChronoUnit.DAYS;
import java.io.Serializable;

public class Contrato extends Documento implements Serializable {
	private static final long serialVersionUID = 1L;

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

	public boolean consultarVigencia(LocalDate fecha) {
		return fecha.isBefore(fechaFin) && fecha.isAfter(fechaInicio);
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
		return DAYS.between(fechaInicio, LocalDate.now());

	}
}
