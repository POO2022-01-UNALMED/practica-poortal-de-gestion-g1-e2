package gestorAplicacion;

import java.time.LocalDate;

public abstract class Documento {
	protected LocalDate fechaExpedicion;

	public Documento() {
		this.fechaExpedicion = LocalDate.now();
	}

	public LocalDate getFechaExpedicion() {
		return fechaExpedicion;
	}

	abstract String generarIdentificador();
}
