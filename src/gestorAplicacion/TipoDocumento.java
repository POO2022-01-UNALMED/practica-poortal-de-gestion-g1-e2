package gestorAplicacion;

public enum TipoDocumento {
	CC("C�dula de Ciudadania"), CE("Cedula de Extranjer�a"), NIP("Numero de Identificaci�n"),
	TI("Tarjeta de Identidad"), PAP("Pasaporte");

	public final String label;

	TipoDocumento(String label) {
		this.label = label;
	}
}
