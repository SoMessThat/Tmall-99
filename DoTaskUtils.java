import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * @author GJ
 * @create 19/10/29 12:52
 * @Description
 **/
public class DoTaskUtils {

    /**
     * 按钮距离手机左侧像素点距离
     */
    private static final int WIDTH = 900;
    /**
     * 分别存放主会场、其他会场、主好货、其他好货、20个店铺按钮距离顶部距离
     */
    private static final int[] HEIGHT = {1160, 1350, 1540, 1725, 1900};

    public void swipeScreen() throws InterruptedException {
        // 滑动屏幕
        this.execCMD("adb shell input swipe 900 1500 900 1000");
        Thread.sleep(2000);
        this.execCMD("adb shell input swipe 900 1500 900 1000");
        Thread.sleep(1000);
        this.execCMD("adb shell input swipe 900 1500 900 1000");
    }

    public void back() {
        this.execCMD("adb shell input keyevent KEYCODE_BACK");
    }

    public void meetingPlace() throws InterruptedException {
        System.out.println("浏览主会场");
        for (int i = 1; i < 4; i++) {
            // 点击进入浏览
            this.execCMD("adb shell input tap " + WIDTH + " " + HEIGHT[0]);
            this.swipeScreen();
            Thread.sleep(20000);
            this.back();
        }
        System.out.println("浏览主会场完成，开始浏览其他会场");
        for (int i = 1; i < 4; i++) {
            // 点击进入浏览
            this.execCMD("adb shell input tap " + WIDTH + " " + HEIGHT[1]);
            this.swipeScreen();
            Thread.sleep(20000);
            this.back();
        }
    }

    public void meetingGood() throws InterruptedException {
        System.out.println("浏览好货");
        for (int i = 1; i < 4; i++) {
            // 点击进入浏览
            this.execCMD("adb shell input tap " + WIDTH + " " + HEIGHT[2]);
            this.swipeScreen();
            Thread.sleep(20000);
            this.back();
        }
        System.out.println("浏览好货完成，开始浏览其他货");
        for (int i = 1; i < 4; i++) {
            // 点击进入浏览
            this.execCMD("adb shell input tap " + WIDTH + " " + HEIGHT[3]);
            this.swipeScreen();
            Thread.sleep(20000);
            this.back();
        }
    }

    public void enter20Time() throws InterruptedException {
        for (int i = 1; i < 20; i++) {
            System.out.println("===== 逛*****店({" + i + "}/20) ======");
            this.execCMD("adb shell input tap " + WIDTH + " " + HEIGHT[4]);
            Thread.sleep(2000);
            this.swipeScreen();
            System.out.println("进入店铺，浏览中，请等待 18 秒");
            Thread.sleep(20000);
            this.back();
        }
        System.out.println("已逛完20个店铺任务");
    }

    public static void main(String[] args) throws InterruptedException {
        DoTaskUtils doTaskUtils = new DoTaskUtils();
        doTaskUtils.enter20Time();
        doTaskUtils.meetingGood();
        doTaskUtils.meetingPlace();
    }

    /**
     * 获取执行结果
     *
     * @param command
     * @return
     */
    public String execCMD(String command) {
        StringBuilder sb = new StringBuilder();
        try {
            Process process = Runtime.getRuntime().exec(command);
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line + "\n");
            }
        } catch (Exception e) {
            return e.toString();
        }
        return sb.toString();
    }
}
