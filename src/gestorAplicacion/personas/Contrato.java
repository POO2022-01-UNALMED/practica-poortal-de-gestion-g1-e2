package gestorAplicacion.personas;

import java.time.LocalDate;

import gestorAplicacion.general.Documento;

import static java.time.temporal.ChronoUnit.DAYS;
import java.io.Serializable;

/**
 * Esta clase extiende de Documento y tiene como finalidad
 * 
 * @author Mateo Alvarez Lebrum
 * @author Alejandro Alvarez Botero
 * @author Miguel Angel Barrera Bustamante
 * @author Alejandra Barrientos Grisales
 */

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
    
	/**
	 * Verificar que el empleado este activo en la empresa, teniendo en cuenta que
	 *el dia actual debe ser mayor al inicio del contrato y menor a la fecha fin
	 *del contrato
	 * @param fechaSolicitud
	 * @return boolean
	 */
	
	public boolean consultarVigencia(LocalDate fecha) {
		return (fecha.isBefore(fechaFin) && fecha.isAfter(fechaInicio)) || 
				fecha.isEqual(fechaInicio);
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

	/**
	 * Generar aleatoriamente un número de identificación
	 * @return text
	 */
	protected String generarIdentificador() {
		String text = "";
		for (int i = 0; i < 5; i++) {
			text += ((int) (Math.random() * 10)) + "";
		}
		return text;
	}
    
	/**
	 * Cacular la cantidad de dias entre el inicio del contrato y la fecha actual
	 * @return text
	 */
	public long cantidadDiasEmpresa() {
		return DAYS.between(fechaInicio, LocalDate.now());

	}
}
