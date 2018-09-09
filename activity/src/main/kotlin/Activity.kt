import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Activity(
    val name: String,
    val profileVelocity: Int,
    val profileDistance: Int,
        var actualDistance: Int = 0,
    val data: MutableList<List<Int>> = mutableListOf(),
    val meta: MutableMap<String, String> = mutableMapOf()
)