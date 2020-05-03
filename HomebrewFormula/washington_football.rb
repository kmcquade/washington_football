class WashingtonFootball < Formula
  include Language::Python::Virtualenv

  desc "Shiny new formula"
  homepage "https://github.com/kmcquade/washington_football"
  url "https://files.pythonhosted.org/packages/d8/e3/a265ec74af09b05fba097ef65d9adbefafbb2b539a8e419763ff6c42eff0/washington_football-0.0.17.0.tar.gz"
  sha256 "29acd182dc834c6fc751d9415cad24d1f1213dff9db64d33db1d37e24a1d48e8"

  depends_on "python3"

  resource "click" do
    url "https://files.pythonhosted.org/packages/27/6f/be940c8b1f1d69daceeb0032fee6c34d7bd70e3e649ccac0951500b4720e/click-7.1.2.tar.gz"
    sha256 "d2b5255c7c6349bc1bd1e59e08cd12acbbd63ce649f2588755783aa94dfb6b1a"
  end

  resource "click-log" do
    url "https://files.pythonhosted.org/packages/22/44/3d73579b547f0790a2723728088c96189c8b52bd2ee3c3de8040efc3c1b8/click-log-0.3.2.tar.gz"
    sha256 "16fd1ca3fc6b16c98cea63acf1ab474ea8e676849dc669d86afafb0ed7003124"
  end

  def install
    virtualenv_create(libexec, "python3")
    virtualenv_install_with_resources
  end

  test do
    false
  end
end
