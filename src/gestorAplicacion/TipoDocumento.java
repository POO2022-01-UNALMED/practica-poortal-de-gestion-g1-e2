package gestorAplicacion;

public enum TipoDocumento {
	CC("C�dula de Ciudadan�a"), CE("C�dula de Extranjer�a"), NIP("N�mero de Identificaci�n"),
	TI("Tarjeta de Identidad"), PAP("Pasaporte");

	public final String label;

	TipoDocumento(String label) {
		this.label = label;
	}
}
