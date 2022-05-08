package gestorAplicacion;

public enum TipoDocumento {
	CC("Cédula de Ciudadanía"), CE("Cédula de Extranjería"), NIP("Número de Identificación"),
	TI("Tarjeta de Identidad"), PAP("Pasaporte");

	public final String label;

	TipoDocumento(String label) {
		this.label = label;
	}
}
