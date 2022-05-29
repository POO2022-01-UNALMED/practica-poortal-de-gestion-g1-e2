package gestorAplicacion;

public enum TipoDocumento {
	CC("Cédula de Ciudadania"), CE("Cedula de Extranjería"), NIP("Numero de Identificación"),
	TI("Tarjeta de Identidad"), PAP("Pasaporte");

	public final String label;

	TipoDocumento(String label) {
		this.label = label;
	}
}
