import com.github.kittinunf.fuel.httpPost
import com.squareup.moshi.Moshi

const val POST = "http://127.0.0.1:5000/load"

fun main(args: Array<String>) {
    val activity = Activity("First Test Run", 12_000, 250_000)
    val wheelList = listOf("colson", "magic")
    val directionList = listOf(-90.0, 0.0, 90.0, 180.0)

    // id,motion_activity_id,milliseconds,profile_acceleration,profile_velocity,profile_ticks,actual_ticks,forward,strafe,azimuth
    activity.data.add(listOf(20.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    activity.data.add(listOf(40.0, 120000.0, 2400.0, 24.0, 0.0, 0.006, 0.0, 0.0))
    activity.data.add(listOf(60.0, 240000.0, 7200.0, 120.0, 0.0, 0.018, 0.0, 0.0))
    activity.data.add(listOf(80.0, 360000.0, 14400.0, 336.0, 0.0, 0.036, 0.0, 0.0))
    activity.data.add(listOf(100.0, 480000.0, 24000.0, 720.0, 0.0, 0.06, 0.0, 0.0))
    activity.data.add(listOf(120.0, 600000.0, 36000.0, 1320.0, 38.0, 0.09, 0.0, 0.0))
    activity.data.add(listOf(140.0, 600000.0, 48000.0, 2160.0, 113.0, 0.12, 0.0, 0.0))
    activity.data.add(listOf(160.0, 600000.0, 60000.0, 3240.0, 254.0, 0.15, 0.0, 0.0))
    activity.data.add(listOf(180.0, 600000.0, 72000.0, 4560.0, 401.0, 0.18, 0.0, 0.0))
    activity.data.add(listOf(200.0, 600000.0, 84000.0, 6120.0, 712.0, 0.21, 0.0, 0.0))
    activity.data.add(listOf(220.0, 600000.0, 96000.0, 7920.0, 1155.0, 0.24, 0.0, 0.0))
    activity.data.add(listOf(240.0, 480000.0, 105600.0, 9936.0, 1787.0, 0.264, 0.0, 0.0))
    activity.data.add(listOf(260.0, 360000.0, 112800.0, 12120.0, 2639.0, 0.282, 0.0, 0.0))
    activity.data.add(listOf(280.0, 240000.0, 117600.0, 14424.0, 3638.0, 0.294, 0.0, 0.0))
    activity.data.add(listOf(300.0, 120000.0, 120000.0, 16800.0, 4791.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(320.0, 0.0, 120000.0, 19200.0, 6115.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(340.0, 0.0, 120000.0, 21600.0, 7702.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(360.0, 0.0, 120000.0, 24000.0, 9518.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(380.0, 0.0, 120000.0, 26400.0, 11388.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(400.0, 0.0, 120000.0, 28800.0, 13289.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(420.0, 0.0, 120000.0, 31200.0, 15219.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(440.0, 0.0, 120000.0, 33600.0, 16691.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(460.0, 0.0, 120000.0, 36000.0, 18743.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(480.0, 0.0, 120000.0, 38400.0, 20813.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(500.0, 0.0, 120000.0, 40800.0, 22986.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(520.0, 0.0, 120000.0, 43200.0, 25203.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(540.0, 0.0, 120000.0, 45600.0, 27423.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(560.0, 0.0, 120000.0, 48000.0, 29687.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(580.0, 0.0, 120000.0, 50400.0, 32001.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(600.0, 0.0, 120000.0, 52800.0, 34303.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(620.0, 0.0, 120000.0, 55200.0, 36678.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(640.0, 0.0, 120000.0, 57600.0, 39099.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(660.0, 0.0, 120000.0, 60000.0, 41358.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(680.0, 0.0, 120000.0, 62400.0, 43811.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(700.0, 0.0, 120000.0, 64800.0, 46210.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(720.0, 0.0, 120000.0, 67200.0, 48585.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(740.0, 0.0, 120000.0, 69600.0, 51076.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(760.0, 0.0, 120000.0, 72000.0, 53549.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(780.0, 0.0, 120000.0, 74400.0, 55942.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(800.0, 0.0, 120000.0, 76800.0, 58450.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(820.0, 0.0, 120000.0, 79200.0, 60904.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(840.0, 0.0, 120000.0, 81600.0, 63401.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(860.0, 0.0, 120000.0, 84000.0, 65880.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(880.0, 0.0, 120000.0, 86400.0, 68347.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(900.0, 0.0, 120000.0, 88800.0, 70806.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(920.0, 0.0, 120000.0, 91200.0, 73231.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(940.0, 0.0, 120000.0, 93600.0, 75676.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(960.0, 0.0, 120000.0, 96000.0, 78080.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(980.0, 0.0, 120000.0, 98400.0, 80462.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1000.0, 0.0, 120000.0, 100800.0, 82943.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1020.0, 0.0, 120000.0, 103200.0, 85348.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1040.0, 0.0, 120000.0, 105600.0, 87816.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1060.0, 0.0, 120000.0, 108000.0, 90352.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1080.0, 0.0, 120000.0, 110400.0, 92821.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1100.0, 0.0, 120000.0, 112800.0, 95316.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1120.0, 0.0, 120000.0, 115200.0, 97810.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1140.0, 0.0, 120000.0, 117600.0, 100261.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1160.0, 0.0, 120000.0, 120000.0, 102698.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1180.0, 0.0, 120000.0, 122400.0, 105108.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1200.0, 0.0, 120000.0, 124800.0, 107516.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1220.0, 0.0, 120000.0, 127200.0, 109947.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1240.0, 0.0, 120000.0, 129600.0, 112311.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1260.0, 0.0, 120000.0, 132000.0, 114686.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1280.0, 0.0, 120000.0, 134400.0, 117046.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1300.0, 0.0, 120000.0, 136800.0, 119402.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1320.0, 0.0, 120000.0, 139200.0, 121762.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1340.0, 0.0, 120000.0, 141600.0, 124119.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1360.0, 0.0, 120000.0, 144000.0, 126476.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1380.0, 0.0, 120000.0, 146400.0, 128848.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1400.0, 0.0, 120000.0, 148800.0, 131221.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1420.0, 0.0, 120000.0, 151200.0, 133610.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1440.0, 0.0, 120000.0, 153600.0, 136013.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1460.0, 0.0, 120000.0, 156000.0, 138410.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1480.0, 0.0, 120000.0, 158400.0, 140839.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1500.0, 0.0, 120000.0, 160800.0, 143218.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1520.0, 0.0, 120000.0, 163200.0, 145625.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1540.0, 0.0, 120000.0, 165600.0, 148028.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1560.0, 0.0, 120000.0, 168000.0, 150470.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1580.0, 0.0, 120000.0, 170400.0, 152840.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1600.0, 0.0, 120000.0, 172800.0, 155256.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1620.0, 0.0, 120000.0, 175200.0, 157689.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1640.0, 0.0, 120000.0, 177600.0, 160097.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1660.0, 0.0, 120000.0, 180000.0, 162513.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1680.0, 0.0, 120000.0, 182400.0, 164917.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1700.0, 0.0, 120000.0, 184800.0, 167313.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1720.0, 0.0, 120000.0, 187200.0, 169722.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1740.0, 0.0, 120000.0, 189600.0, 172114.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1760.0, 0.0, 120000.0, 192000.0, 174540.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1780.0, 0.0, 120000.0, 194400.0, 176961.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1800.0, 0.0, 120000.0, 196800.0, 179428.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1820.0, 0.0, 120000.0, 199200.0, 181814.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1840.0, 0.0, 120000.0, 201600.0, 184269.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1860.0, 0.0, 120000.0, 204000.0, 186686.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1880.0, 0.0, 120000.0, 206400.0, 189090.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1900.0, 0.0, 120000.0, 208800.0, 191507.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1920.0, 0.0, 120000.0, 211200.0, 193926.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1940.0, 0.0, 120000.0, 213600.0, 196267.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1960.0, 0.0, 120000.0, 216000.0, 198673.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(1980.0, 0.0, 120000.0, 218400.0, 201070.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2000.0, 0.0, 120000.0, 220800.0, 203435.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2020.0, 0.0, 120000.0, 223200.0, 205786.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2040.0, 0.0, 120000.0, 225600.0, 208133.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2060.0, 0.0, 120000.0, 228000.0, 210471.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2080.0, 0.0, 120000.0, 230400.0, 212805.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2100.0, 0.0, 120000.0, 232800.0, 215142.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2120.0, 0.0, 120000.0, 235200.0, 217472.0, 0.3, 0.0, 0.0))
    activity.data.add(listOf(2140.0, -120000.0, 117600.0, 237576.0, 219811.0, 0.294, 0.0, 0.0))
    activity.data.add(listOf(2160.0, -240000.0, 112800.0, 239880.0, 222172.0, 0.282, 0.0, 0.0))
    activity.data.add(listOf(2180.0, -360000.0, 105600.0, 242064.0, 224537.0, 0.264, 0.0, 0.0))
    activity.data.add(listOf(2200.0, -480000.0, 96000.0, 244080.0, 226885.0, 0.24, 0.0, 0.0))
    activity.data.add(listOf(2220.0, -600000.0, 84000.0, 245880.0, 229192.0, 0.21, 0.0, 0.0))
    activity.data.add(listOf(2240.0, -600000.0, 72000.0, 247440.0, 231424.0, 0.18, 0.0, 0.0))
    activity.data.add(listOf(2260.0, -600000.0, 60000.0, 248760.0, 233509.0, 0.15, 0.0, 0.0))
    activity.data.add(listOf(2280.0, -600000.0, 48000.0, 249840.0, 235488.0, 0.12, 0.0, 0.0))
    activity.data.add(listOf(2300.0, -600000.0, 36000.0, 250680.0, 237332.0, 0.09, 0.0, 0.0))
    activity.data.add(listOf(2320.0, -600000.0, 24000.0, 251280.0, 238951.0, 0.06, 0.0, 0.0))
    activity.data.add(listOf(2340.0, -480000.0, 14400.0, 251664.0, 240427.0, 0.036, 0.0, 0.0))
    activity.data.add(listOf(2360.0, -360000.0, 7200.0, 251880.0, 241675.0, 0.018, 0.0, 0.0))
    activity.data.add(listOf(2380.0, -240000.0, 2400.0, 251976.0, 242796.0, 0.006, 0.0, 0.0))
    activity.data.add(listOf(2400.0, -120000.0, 0.0, 252000.0, 243829.0, 0.0, 0.0, 0.0))

    activity.meta["direction"] = directionList.shuffled().first()
    activity.meta["wheel"] = wheelList.shuffled().first()
    activity.meta["azimuth"] = 0.0
    activity.meta["dt"] = 20
    activity.meta["t1"] = 200
    activity.meta["t2"] = 100
    activity.meta["vProg"] = 120_000

    activity.meta["gyroStart"] = randomRange(-4.0, 4.0)
    activity.meta["gyroEnd"] = randomRange(-4.0, 4.0)

    activity.profileTicks = 250_000
    activity.actualTicks = randomRange(240_000.0, 250_000.0).toInt()
    activity.actualDistance = randomRange(100.0, 108.0)

    val moshi = Moshi.Builder().build()
    val adapter = ActivityJsonAdapter(moshi)

    val (_, _, result) = POST.httpPost()
        .header("content-type" to "application/json")
        .body(adapter.toJson(activity))
        .responseString()

    println(result.get())
}

fun randomRange(min: Double, max: Double) = min + Math.random() * (max - min)