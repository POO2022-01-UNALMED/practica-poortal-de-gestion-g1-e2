package gestorAplicacion;

import java.time.LocalDate;

public abstract class Documento {
	protected LocalDate fechaExpedicion;

	public Documento() {
		this(LocalDate.now());
	}
	
	public Documento(LocalDate fecha) {
		this.fechaExpedicion = fecha;
	}

	public LocalDate getFechaExpedicion() {
		return fechaExpedicion;
	}

	abstract String generarIdentificador();
}
