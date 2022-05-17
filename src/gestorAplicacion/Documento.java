package gestorAplicacion;

import java.time.LocalDate;

public abstract class Documento {
	protected LocalDate fechaExpedicion;

	public Documento() {
		this.fechaExpedicion = LocalDate.now();
	}

	abstract String generarIdentificador();
}
