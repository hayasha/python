import java.util.*;

class Virus implements Comparable<Virus> {

    private int x;
    private int y;
    private int level;
    private int time;

    // movement
    private int[] dx = { -1, 0, 1, 0 };
    private int[] dy = { 0, 1, 0, -1 };

    public Virus(int x, int y, int level, int time) {
        this.x = x;
        this.y = y;
        this.level = level;
        this.time = time;
    }

    public void move(int[][] graph, Queue<Virus> q) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 1 && nx < graph.length && ny >= 1 && ny < graph.length) {
                if (graph[nx][ny] == 0) {
                    graph[nx][ny] = level;
                    q.offer(new Virus(nx, ny, level, time + 1));
                }
            }
        }
    }

    public boolean isTimeOver(int time) {
        return this.time == time;
    }

    // 오름차순 정렬
    @Override
    public int compareTo(Virus another) {
        return this.level < another.level ? -1 : 1;
    }
}

public class Main {

    public static int N, K, S, X, Y;
    public static int[][] graph = new int[201][201];
    public static ArrayList<Virus> viruses = new ArrayList<Virus>();

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();

        // graph init
        // Virus waiting list
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                graph[i][j] = sc.nextInt();
                if (graph[i][j] != 0) {
                    viruses.add(new Virus(i, j, graph[i][j], 0));
                }
            }
        }

        S = sc.nextInt();
        X = sc.nextInt();
        Y = sc.nextInt();

        Collections.sort(viruses);
        Queue<Virus> q = new LinkedList<>();
        for (int i = 0; i < viruses.size(); i++) {
            q.offer(viruses.get(i));
        }

        while (!q.isEmpty()) {
            Virus virus = q.poll();
            if (virus.isTimeOver(S)) break;

            virus.move(graph, q);
        }

        System.out.println(graph[X][Y]);
    }
}