import com.github.kittinunf.fuel.httpPost
import com.squareup.moshi.JsonClass
import com.squareup.moshi.Moshi

@JsonClass(generateAdapter = true)
data class Activity(
    val name: String,
    val activityMeasures: List<String> = listOf("profile_ticks", "actual_ticks", "actual_distance"),
    val activityData: MutableList<Double> = mutableListOf(),
    val traceMeasures: List<String> = listOf(
        "profile_acc",
        "profile_vel",
        "profile_ticks",
        "actual_ticks",
        "foward",
        "strafe",
        "azimuth"
    ),
    val traceData: MutableList<List<Double>> = mutableListOf(),
    val meta: MutableMap<String, Any> = mutableMapOf()
)

fun Activity.upload() {
    val moshi = Moshi.Builder().build()
    val adapter = ActivityJsonAdapter(moshi)

    val (_, _, result) = POST.httpPost()
        .header("content-type" to "application/json")
        .body(adapter.toJson(this))
        .responseString()

    println(result.get())

}
