package gestorAplicacion.ventas;

public enum Categoria {
	ASEO("Aseo"), ROPA("Ropa"), ALIMENTACION("Alimentacion"), MASCOTA("Mascota"), SALUD("Salud"),
	TECNOLOGIA("Tecnologia");

	public final String label;

	Categoria(String label) {
		this.label = label;
	}
}
