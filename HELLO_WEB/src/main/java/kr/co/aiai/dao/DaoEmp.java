package kr.co.aiai.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class DaoEmp {

	public EmpVO getOne(EmpVO pvo) throws Exception {

		EmpVO rvo = new EmpVO();

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();

		String sql = "select e_id,e_name,sex,addr from emp "; // *보단 필드값으로 명시해주는것이 좋은 습관이다
		sql += "where ";
		sql += "e_id = '" + pvo.getE_id() + "' ";

		ResultSet rs = stmt.executeQuery(sql);

		while (rs.next()) {

			rvo.setE_id(rs.getString("e_id"));
			rvo.setE_name(rs.getString("e_name"));
			rvo.setSex(rs.getString("sex"));
			rvo.setAddr(rs.getString("addr"));
		}
		
		rs.close();
		stmt.close();
		conn.close();
		
		return rvo;
	}

	public ArrayList<EmpVO> getList() throws Exception {

		ArrayList<EmpVO> list = new ArrayList<EmpVO>();

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "select * from emp";

		ResultSet rs = stmt.executeQuery(sql);

		while (rs.next()) {
			String e_id = rs.getString("e_id");
			String e_name = rs.getString("e_name");
			String sex = rs.getString("sex");
			String addr = rs.getString("addr");
//			System.out.println("e_id" + e_id + " , " + "e_name = " + e_name);
			EmpVO temp = new EmpVO();
			temp.setE_id(e_id);
			temp.setE_name(e_name);
			temp.setSex(sex);
			temp.setAddr(addr);
			list.add(temp);

		}

		rs.close();
		stmt.close();
		conn.close();

		return list;
	}

	public int insert(EmpVO vo) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();

		String sql = "insert into emp ";
		sql += "(e_name,sex,addr) ";
		sql += "values ";
		sql += "('"  + vo.getE_name() + "','" + vo.getSex() + "','" + vo.getAddr() + "')";
		int cnt = stmt.executeUpdate(sql);
		return cnt;
	}

	public int update(EmpVO vo) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "";
		sql += "update emp ";
		sql += "set ";
		sql += "e_name = '" + vo.getE_name() + "', ";
		sql += "sex = '" + vo.getSex() + "', ";
		sql += "addr = '" + vo.getAddr() + "' ";
		sql += "where ";
		sql += "e_id = '" + vo.getE_id() + "' ";
		int cnt = stmt.executeUpdate(sql);
		return cnt;
	}

	public int delete(EmpVO vo) throws Exception {

		Class.forName("com.mysql.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		String sql = "";
		sql += "delete from emp ";
		sql += "where ";
		sql += "e_id = '" + vo.getE_id() + "' ";
		int cnt = stmt.executeUpdate(sql);
		return cnt;
	}

	public static void main(String[] args) throws Exception {
		DaoEmp de = new DaoEmp();
		EmpVO vo = de.getOne(new EmpVO("1","4","4","4"));
		System.out.println("vo :" + vo);
	}
}
